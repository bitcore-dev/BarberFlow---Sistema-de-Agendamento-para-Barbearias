
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Autenticação
    path("cadastro/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/auth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # Painel do usuário
    path("painel/", views.dashboard, name="dashboard"),

    # Barbearias
    path(
        "barbearia/<int:pk>/",
        views.barbershop_detail,
        name="barbershop_detail",
    ),

    # Reservas
    path(
        "barbearia/<int:pk>/reservar/",
        views.create_booking,
        name="create_booking",
    ),
    path(
        "minhas-reservas/<int:pk>/",
        views.booking_detail,
        name="booking_detail",
    ),

    path(
    "painel/barbearia/nova/",
    views.create_barbershop,
    name="create_barbershop",
),
]
