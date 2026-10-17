
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

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
