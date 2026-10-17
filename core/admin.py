
from django.contrib import admin
from .models import Barbershop, Barber, Service, UserProfile


@admin.register(Barbershop)
class BarbershopAdmin(admin.ModelAdmin):
    list_display = ("name", "neighborhood", "city", "owner", "is_active")
    search_fields = ("name", "neighborhood", "city")
    list_filter = ("is_active", "city")


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ("name", "barbershop", "is_active")
    search_fields = ("name", "barbershop__name")
    list_filter = ("is_active",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "barbershop",
        "price",
        "estimated_duration_minutes",
        "is_active",
    )
    search_fields = ("name", "barbershop__name")
    list_filter = ("is_active",)

    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "created_at")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email")
