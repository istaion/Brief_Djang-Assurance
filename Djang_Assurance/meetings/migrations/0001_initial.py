# Generated by Django 5.1.5 on 2025-01-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Appointment",
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
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Availability",
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
                    "day_of_week",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ]
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
    ]
