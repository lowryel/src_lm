# Generated by Django 4.2.2 on 2023-07-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lmestate", "0009_rename_image_imagemodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="property",
            name="image",
        ),
        migrations.DeleteModel(
            name="ImageModel",
        ),
        migrations.AddField(
            model_name="property",
            name="image",
            field=models.ImageField(default=1, upload_to="img"),
            preserve_default=False,
        ),
    ]
