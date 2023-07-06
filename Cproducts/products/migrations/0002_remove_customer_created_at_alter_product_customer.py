# Generated by Django 4.2.3 on 2023-07-06 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="customer", name="created_at",),
        migrations.AlterField(
            model_name="product",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prdcts",
                to="products.customer",
            ),
        ),
    ]
