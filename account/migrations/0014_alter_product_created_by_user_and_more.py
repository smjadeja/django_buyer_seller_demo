# Generated by Django 4.1.2 on 2022-10-19 12:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_myuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by_user',
            field=models.ForeignKey(error_messages={'required': 'Please select user type'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.myuser'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_cost_price',
            field=models.IntegerField(error_messages={'required': 'Please enter cost price'}, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_sell_price',
            field=models.IntegerField(error_messages={'required': 'Please sell price'}, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(error_messages={'required': 'Enter product description'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(error_messages={'required': 'Please upload an image'}, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(error_messages={'required': 'Enter product name'}, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_unit',
            field=models.IntegerField(error_messages={'required': 'Please enter stock unit'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
