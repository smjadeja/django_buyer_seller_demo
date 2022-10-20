# Generated by Django 4.1.2 on 2022-10-19 10:30

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_myuser_balance_alter_user_purchase_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='balance',
            field=models.FloatField(validators=[account.models.CustomMinvalue(0)]),
        ),
    ]