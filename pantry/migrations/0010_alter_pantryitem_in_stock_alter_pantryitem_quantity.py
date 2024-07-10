# Generated by Django 5.0.6 on 2024-07-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0009_pantryitem_in_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantryitem',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]