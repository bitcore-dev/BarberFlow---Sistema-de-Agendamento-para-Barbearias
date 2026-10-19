
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Barbershop(models.Model):
    owner = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.PROTECT,
    related_name="barbershop",
    verbose_name="proprietário",
)
    name = models.CharField("nome", max_length=120)
    description = models.TextField("descrição", blank=True)
    neighborhood = models.CharField("bairro", max_length=100)
    city = models.CharField("cidade", max_length=100)
    address = models.CharField("endereço", max_length=255)
    phone = models.CharField("telefone", max_length=20, blank=True)
    is_active = models.BooleanField("ativa", default=True)
    created_at = models.DateTimeField("criada em", auto_now_add=True)
    daily_capacity = models.PositiveIntegerField("limite diário de clientes",
    default=30,
    validators=[MinValueValidator(1)],
)

    class Meta:
        verbose_name = "barbearia"
        verbose_name_plural = "barbearias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Barber(models.Model):
    barbershop = models.ForeignKey(
        Barbershop,
        on_delete=models.CASCADE,
        related_name="barbers",
        verbose_name="barbearia",
    )
    name = models.CharField("nome", max_length=120)
    bio = models.TextField("apresentação", blank=True)
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "barbeiro"
        verbose_name_plural = "barbeiros"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} — {self.barbershop.name}"


class Service(models.Model):
    barbershop = models.ForeignKey(
        Barbershop,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="barbearia",
    )
    name = models.CharField("nome", max_length=120)
    description = models.TextField("descrição", blank=True)
    price = models.DecimalField(
        "preço",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    estimated_duration_minutes = models.PositiveIntegerField(
        "duração estimada em minutos",
        validators=[MinValueValidator(5)],
    )
    is_active = models.BooleanField("ativo", default=True)

    class Meta:
        verbose_name = "serviço"
        verbose_name_plural = "serviços"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} — R$ {self.price}"


class UserProfile(models.Model):
    class Role(models.TextChoices):
        CUSTOMER = "customer", "Cliente"
        OWNER = "owner", "Proprietário"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    role = models.CharField(
        "tipo de conta",
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )
    created_at = models.DateTimeField(
        "criado em",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "perfil de usuário"
        verbose_name_plural = "perfis de usuários"

    def __str__(self):
        return f"{self.user.username} — {self.get_role_display()}"


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pendente"
        CONFIRMED = "confirmed", "Confirmado"
        CANCELLED = "cancelled", "Cancelado"
        COMPLETED = "completed", "Concluído"
        NO_SHOW = "no_show", "Não compareceu"

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="bookings",
        verbose_name="cliente",
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name="bookings",
        verbose_name="serviço",
    )
    date = models.DateField("dia do atendimento")
    status = models.CharField(
        "situação",
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(
        "solicitado em",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "reserva"
        verbose_name_plural = "reservas"
        ordering = ["date", "created_at"]
        indexes = [
            models.Index(fields=["date", "status"]),
        ]

    def __str__(self):
        return (
            f"{self.customer.username} — "
            f"{self.service.name} — {self.date}"
        )
