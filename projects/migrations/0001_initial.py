# Generated by Django 4.2.7 on 2023-11-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=63)),
                ("description", models.TextField(max_length=1000)),
                ("url", models.URLField()),
            ],
        ),
    ]