# Generated by Django 5.2.1 on 2025-06-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_slider_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                ("question", models.CharField(max_length=255, verbose_name="Питання")),
                ("answer", models.TextField(verbose_name="Відповідь")),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQ (Часті питання)",
                "ordering": ["id"],
            },
        ),
    ]
