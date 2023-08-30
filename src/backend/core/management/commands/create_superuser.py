from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import logging

from core.utils.security import os_getenv


class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        email = os_getenv('SUPERUSER_EMAIL', 'admin@mail.ru')
        username = os_getenv("SUPERUSER_NAME", "adm")
        if not User.objects.filter(email=email).exists():
            super_user = User(
                is_superuser=True,
                is_staff=True,
                email=email,
                username=username,
            )
            super_user.set_password(os_getenv('SUPERUSER_PASSWORD', '123'))
            super_user.save()

            logging.info(f"Superuser '{email}' seed successful! [OK]")
        else:
            logging.error(f"Superuser '{email}' already exits")
