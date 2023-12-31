# Generated by Django 4.2.3 on 2023-07-18 21:40

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Condition",
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
                ("notes", models.TextField(blank=True)),
                ("image", models.ImageField(blank=True, upload_to="conditions")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PointOfInterest",
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
                ("notes", models.TextField(blank=True)),
                (
                    "image",
                    models.ImageField(blank=True, upload_to="point_of_interests"),
                ),
                ("height_m", models.FloatField(null=True)),
                ("installation_date", models.DateField(null=True)),
                ("is_date_estimated", models.BooleanField(default=False)),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(srid=4326),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PointOfInterestType",
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
                ("notes", models.TextField(blank=True)),
                (
                    "image",
                    models.ImageField(blank=True, upload_to="point_of_interest_types"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PointOfInterestCondition",
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
                ("date", models.DateTimeField(auto_now_add=True)),
                ("notes", models.TextField(blank=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="point_of_interest_conditions"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "condition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="farms.condition"
                    ),
                ),
                (
                    "point_of_interest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="farms.pointofinterest",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pointofinterest",
            name="point_of_interest_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="farms.pointofinteresttype",
            ),
        ),
    ]
