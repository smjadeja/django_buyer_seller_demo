# Generated by Django 4.1.2 on 2022-10-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_product_prod_cost_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.myuser'),
        ),
    ]
