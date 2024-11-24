# Generated by Django 5.1.3 on 2024-11-24 04:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("classroomApp", "0004_alter_message_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="avatars/default.png", upload_to="avatars/"
                    ),
                ),
                ("bio", models.TextField(blank=True, max_length=500)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("website", models.URLField(blank=True)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
    ]