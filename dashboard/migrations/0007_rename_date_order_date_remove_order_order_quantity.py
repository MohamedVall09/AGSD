# Generated by Django 4.2.9 on 2024-08-01 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='dAte',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_quantity',
        ),
    ]
