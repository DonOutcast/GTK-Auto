from django.db import models
from django.utils import timezone

from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Country(BaseModel):
    title = models.CharField(
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.title


class City(BaseModel):
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        related_name='cities'
    )

    title = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
