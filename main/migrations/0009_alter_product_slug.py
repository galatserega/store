# Generated by Django 5.2.1 on 2025-06-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(),
        ),
    ]
