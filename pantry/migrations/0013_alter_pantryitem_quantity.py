# Generated by Django 5.0.6 on 2024-07-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0012_alter_pantryitem_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantryitem',
            name='quantity',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
