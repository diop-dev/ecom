# Generated by Django 4.2.2 on 2023-08-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_commande_alter_product_options_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="commande",
            name="total",
            field=models.CharField(default="500", max_length=200),
            preserve_default=False,
        ),
    ]
