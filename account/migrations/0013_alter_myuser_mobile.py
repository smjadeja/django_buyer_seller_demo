# Generated by Django 4.1.2 on 2022-10-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_myuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]