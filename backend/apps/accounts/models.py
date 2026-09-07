from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = "CLIENT", "Client"
        PROVIDER = "PROVIDER", "Prestataire"
        ADMIN = "ADMIN", "Administrateur"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return f"{self.email} ({self.role})"


class ProviderProfile(models.Model):
    class Category(models.TextChoices):
        SANTE = "SANTE", "Santé"
        BEAUTE = "BEAUTE", "Beauté"
        SPORT = "SPORT", "Sport"
        COURS = "COURS", "Cours"
        AUTRE = "AUTRE", "Autre"

    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="provider_profile",
    )
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.AUTRE,
    )
    is_validated = models.BooleanField(default=False)

    def __str__(self):
        return f"Profil prestataire de {self.user.email}"