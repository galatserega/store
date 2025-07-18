# Generated by Django 5.2.1 on 2025-06-11 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_product_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="slider",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sliders",
                to="main.product",
            ),
        ),
    ]
