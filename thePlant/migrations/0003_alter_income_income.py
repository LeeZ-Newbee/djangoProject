# Generated by Django 4.2.5 on 2023-09-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thePlant', '0002_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.FloatField(default=0),
        ),
    ]
