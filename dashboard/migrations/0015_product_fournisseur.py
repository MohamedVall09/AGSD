# Generated by Django 4.2.9 on 2024-08-03 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_fournisseur'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fournisseur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.fournisseur'),
            preserve_default=False,
        ),
    ]
