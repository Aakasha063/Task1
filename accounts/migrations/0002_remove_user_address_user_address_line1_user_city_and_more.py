# Generated by Django 4.2.2 on 2023-06-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='address_line1',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], default=None, max_length=1),
        ),
    ]