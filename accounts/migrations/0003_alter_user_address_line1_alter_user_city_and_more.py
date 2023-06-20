# Generated by Django 4.2.2 on 2023-06-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_address_user_address_line1_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address_line1',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]