from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import UserProfile, Booking, Service, Barbershop

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="E-mail",
        required=True,
    )
    role = forms.ChoiceField(
        label="Tipo de conta",
        choices=UserProfile.Role.choices,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "role")

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data["role"],
            )

        return user


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["service", "date"]
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
        }

    def __init__(self, *args, barbershop, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["service"].queryset = Service.objects.filter(
            barbershop=barbershop,
            is_active=True,
        ).order_by("name")

        self.fields["service"].empty_label = "Escolha um serviço"
        self.fields["date"].widget.attrs["min"] = timezone.localdate().isoformat()

    def clean_date(self):
        date = self.cleaned_data["date"]

        if date < timezone.localdate():
            raise forms.ValidationError("Escolha hoje ou uma data futura.")

        return date

class BarbershopForm(forms.ModelForm):
    class Meta:
        model = Barbershop
        fields = [
            "name",
            "description",
            "neighborhood",
            "city",
            "address",
            "phone",
            "daily_capacity",
        ]

        labels = {
            "name": "Nome da barbearia",
            "description": "Descrição",
            "neighborhood": "Bairro",
            "city": "Cidade",
            "address": "Endereço completo",
            "phone": "Telefone para contato",
            "daily_capacity": "Limite diário de clientes",
        }

        help_texts = {
            "daily_capacity": (
                "Número máximo de solicitações de atendimento por dia."
            ),
        }

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "daily_capacity": forms.NumberInput(attrs={"min": 1}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service

        fields = [
            "name",
            "description",
            "price",
            "estimated_duration_minutes",
        ]

        labels = {
            "name": "Nome do serviço",
            "description": "Descrição",
            "price": "Preço (R$)",
            "estimated_duration_minutes": "Duração estimada (minutos)",
        }

        help_texts = {
            "price": "Informe o preço cobrado pelo serviço.",
            "estimated_duration_minutes": (
                "Tempo aproximado para realizar o atendimento."
            ),
        }

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 3}
            ),
            "price": forms.NumberInput(
                attrs={
                    "min": "0",
                    "step": "0.01",
                    "placeholder": "0.00",
                }
            ),
            "estimated_duration_minutes": forms.NumberInput(
                attrs={
                    "min": 5,
                    "step": 5,
                }
            ),
        }

