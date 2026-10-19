
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import RegistrationForm, BookingForm, BarbershopForm
from .models import UserProfile, Barbershop, Service, Booking
from django.db.models import Q
from django.shortcuts import render
from .models import Barbershop


def home(request):
    termo = request.GET.get("bairro", "").strip()

    barbearias = Barbershop.objects.filter(is_active=True)

    if termo:
        barbearias = barbearias.filter(
            Q(name__icontains=termo)
            | Q(neighborhood__icontains=termo)
            | Q(city__icontains=termo)
        )

    barbearias = barbearias.order_by("name")

    return render(
        request,
        "core/index.html",
        {
            "barbearias": barbearias,
            "termo": termo,
            "pesquisou": bool(termo),
        },
    )


def login_view(request):
    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
            ):
                return redirect(next_url)

            return redirect("dashboard")
    else:
        form = AuthenticationForm(request)

    return render(
        request,
        "core/auth/login.html",
        {
            "form": form,
            "next": next_url,
        },
    )



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        else:
            print("ERROS DO CADASTRO:", form.errors)

    else:
        form = RegistrationForm()

    return render(request, "core/auth/register.html", {"form": form})

def barbershop_detail(request, pk):
    barbearia = get_object_or_404(
        Barbershop,
        pk=pk,
        is_active=True,
    )

    servicos = Service.objects.filter(
        barbershop=barbearia,
        is_active=True,
    ).order_by("name")

    return render(
        request,
        "core/barbershop_detail.html",
        {
            "barbearia": barbearia,
            "servicos": servicos,
        },
    )


@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={"role": UserProfile.Role.CUSTOMER},
    )

    if profile.role == UserProfile.Role.OWNER:
        barbearias = Barbershop.objects.filter(
            owner=request.user
        )

        return render(
            request,
            "core/dashboard_owner.html",
            {"barbearias": barbearias},
        )

    reservas = (
        Booking.objects
        .filter(customer=request.user)
        .select_related("service", "service__barbershop")
        .order_by("-date", "-created_at")
    )

    return render(
        request,
        "core/dashboard_customer.html",
        {"reservas": reservas},
    )


@login_required
def create_barbershop(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={"role": UserProfile.Role.CUSTOMER},
    )

    # Somente proprietários podem cadastrar barbearias.
    if profile.role != UserProfile.Role.OWNER:
        return redirect("dashboard")

    # Cada proprietário pode cadastrar apenas uma barbearia.
    if Barbershop.objects.filter(owner=request.user).exists():
        return redirect("dashboard")

    if request.method == "POST":
        form = BarbershopForm(request.POST)

        if form.is_valid():
            barbearia = form.save(commit=False)
            barbearia.owner = request.user
            barbearia.save()

            return redirect("dashboard")
    else:
        form = BarbershopForm()

    return render(
        request,
        "core/barbershop_form.html",
        {"form": form},
    )


@login_required
def create_booking(request, pk):
    barbearia = get_object_or_404(
        Barbershop,
        pk=pk,
        is_active=True,
    )

    if request.method == "POST":
        form = BookingForm(
            request.POST,
            barbershop=barbearia,
        )

        if form.is_valid():
            with transaction.atomic():
                # Serializa as reservas desta barbearia
                # quando o banco suporta bloqueio de linhas.
                barbearia = get_object_or_404(
                    Barbershop.objects.select_for_update(),
                    pk=pk,
                    is_active=True,
                )

                servico = get_object_or_404(
                    Service,
                    pk=form.cleaned_data["service"].pk,
                    barbershop=barbearia,
                    is_active=True,
                )

                data = form.cleaned_data["date"]

                reservas_ativas = Booking.objects.filter(
                    service__barbershop=barbearia,
                    date=data,
                    status__in=[
                        Booking.Status.PENDING,
                        Booking.Status.CONFIRMED,
                    ],
                ).count()

                if reservas_ativas >= barbearia.daily_capacity:
                    form.add_error(
                        None,
                        "A capacidade para esse dia foi atingida. "
                        "Escolha outra data.",
                    )
                else:
                    reserva = form.save(commit=False)
                    reserva.customer = request.user
                    reserva.service = servico
                    reserva.status = Booking.Status.PENDING
                    reserva.save()

                    return redirect(
                        "booking_detail",
                        pk=reserva.pk,
                    )
    else:
        form = BookingForm(barbershop=barbearia)

    return render(
        request,
        "core/booking_form.html",
        {
            "barbearia": barbearia,
            "form": form,
        },
    )


@login_required
def booking_detail(request, pk):
    reserva = get_object_or_404(
        Booking.objects.select_related(
            "service",
            "service__barbershop",
        ),
        pk=pk,
        customer=request.user,
    )

    return render(
        request,
        "core/booking_detail.html",
        {"reserva": reserva},
    )
