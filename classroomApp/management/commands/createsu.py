from django.core.management.base import BaseCommand #type: ignore
from django.contrib.auth.models import User #type: ignore
import os
from dotenv import load_dotenv #type: ignore
load_dotenv()

class Command(BaseCommand):
    help = "Create a superuser if it does not exist"

    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_USERNAME", "admin")
        email = os.getenv("ADMIN_EMAIL", "hs2.zer04@gmail.com")
        password = os.getenv("ADMIN_PASSWORD", "adminadmin")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
