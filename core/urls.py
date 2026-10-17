
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
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
    path("painel/", views.dashboard, name="dashboard"),
    
path(
    "barbearia/<int:pk>/",
    views.barbershop_detail,
    name="barbershop_detail",
),

]
