# Generated by Django 4.2.2 on 2023-08-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmestate", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="enquiry",
            options={"verbose_name": "Enquiry", "verbose_name_plural": "Enquiry"},
        ),
        migrations.AlterField(
            model_name="enquiry",
            name="email",
            field=models.EmailField(help_text="Enter a valid email", max_length=254),
        ),
    ]
