# Generated by Django 4.2.5 on 2023-09-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thePlant', '0003_alter_income_income'),
    ]

    operations = [
        migrations.DeleteModel(
            name='income',
        ),
        migrations.AddField(
            model_name='profit',
            name='date',
            field=models.DateField(default='2023-09-20'),
        ),
    ]