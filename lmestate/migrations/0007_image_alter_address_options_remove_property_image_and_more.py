# Generated by Django 4.2.2 on 2023-07-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmestate", "0006_alter_property_property_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("file", models.ImageField(upload_to="images")),
            ],
        ),
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Address", "verbose_name_plural": "Address"},
        ),
        migrations.RemoveField(
            model_name="property",
            name="image",
        ),
        migrations.AddField(
            model_name="property",
            name="image",
            field=models.ManyToManyField(blank=True, to="lmestate.image"),
        ),
    ]
