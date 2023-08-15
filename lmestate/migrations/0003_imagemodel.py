# Generated by Django 4.2.2 on 2023-08-06 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("lmestate", "0002_alter_enquiry_options_alter_enquiry_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageModel",
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
                ("file", models.ImageField(upload_to="img")),
                ("image_count", models.IntegerField()),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lmestate.property",
                    ),
                ),
            ],
        ),
    ]