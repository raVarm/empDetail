# Generated by Django 4.1 on 2022-08-10 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empDetail', '0003_remove_employee_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
