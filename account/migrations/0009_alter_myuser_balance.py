# Generated by Django 4.1.2 on 2022-10-18 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_purchase_purchased_by_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='balance',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]