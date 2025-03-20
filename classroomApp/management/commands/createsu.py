from django.core.management.base import BaseCommand #type: ignore
from django.contrib.auth.models import User #type: ignore
import os
from dotenv import load_dotenv #type: ignore

load_dotenv()

class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser {username} created successfully!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser {username} already exists."))
