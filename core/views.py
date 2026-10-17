
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RegistrationForm
from .models import UserProfile, Barbershop, Service


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



def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistrationForm()

    return render(
        request,
        "core/auth/register.html",
        {"form": form},
    )

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
        return render(request, "core/dashboard_owner.html")

    return render(request, "core/dashboard_customer.html")
