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
