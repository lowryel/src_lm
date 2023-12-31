# Generated by Django 4.2.2 on 2023-07-31 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("address_line1", models.CharField(max_length=120)),
                ("address_line2", models.CharField(max_length=120)),
                ("city", models.CharField(max_length=120)),
                ("popular_landmark", models.CharField(max_length=120)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Address",
            },
        ),
        migrations.CreateModel(
            name="Agency",
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
                ("agency_name", models.CharField(max_length=120, null=True)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("property_count", models.IntegerField(default=0)),
                ("agency_image", models.ImageField(upload_to="img")),
                ("date_registered", models.DateTimeField(auto_now_add=True)),
                (
                    "agent",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "agent_location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lmestate.address",
                    ),
                ),
            ],
            options={
                "verbose_name": "Agent",
                "verbose_name_plural": "Agency",
            },
        ),
        migrations.CreateModel(
            name="Property",
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
                ("property_id", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("property_location", models.CharField(max_length=512, null=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default="0.00", max_digits=10
                    ),
                ),
                ("description", models.TextField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="img")),
                (
                    "status",
                    models.CharField(
                        choices=[("For Sale", "For Sale"), ("Rent", "Rent")],
                        default="For Sale",
                        max_length=64,
                    ),
                ),
                (
                    "agency",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lmestate.agency",
                    ),
                ),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="Enquiry",
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
                    "email",
                    models.EmailField(help_text="Input a valid email", max_length=254),
                ),
                ("description", models.TextField()),
                ("quote", models.IntegerField(help_text="Quote a figure")),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "property",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lmestate.property",
                    ),
                ),
            ],
        ),
    ]
