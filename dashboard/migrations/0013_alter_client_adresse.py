# Generated by Django 4.2.9 on 2024-08-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_client_adresse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='adresse',
            field=models.CharField(max_length=50),
        ),
    ]
