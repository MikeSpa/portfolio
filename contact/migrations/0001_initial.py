# Generated by Django 4.2.7 on 2023-11-13 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=50)),
                ("email_address", models.EmailField(max_length=150)),
                ("subject", models.CharField(max_length=50)),
                ("message", models.TextField(max_length=2000)),
            ],
        ),
    ]
