# Generated by Django 4.1 on 2022-09-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0006_remove_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img_category',
        ),
        migrations.AddField(
            model_name='category',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app_product.product'),
        ),
    ]
