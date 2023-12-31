from django.db import models
from django.utils.html import format_html

from core.models import BaseModel, Country, City


class Auto(BaseModel):
    price = models.BigIntegerField(
        verbose_name="Цена"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    country = models.ManyToManyField(
        Country,
        related_name="auto_countries"
    )
    city = models.ManyToManyField(
        City,
        related_name="auto_cities"
    )
    image = models.ImageField(
        upload_to="cars",
        verbose_name="Изображение",
    )
    auction = models.BooleanField(
        default=False,
        verbose_name="Торг"
    )


    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
