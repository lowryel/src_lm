# Generated by Django 4.2.2 on 2023-07-18 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmestate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agency",
            name="agency_name",
            field=models.CharField(max_length=120, null=True),
        ),
    ]
