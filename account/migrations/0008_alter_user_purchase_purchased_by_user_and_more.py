# Generated by Django 4.1.2 on 2022-10-18 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_product_created_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_purchase',
            name='purchased_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_by_user', to='account.myuser'),
        ),
        migrations.AlterField(
            model_name='user_purchase',
            name='purchased_from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchased_from_user', to='account.myuser'),
        ),
    ]