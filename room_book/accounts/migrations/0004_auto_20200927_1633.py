# Generated by Django 3.1.1 on 2020-09-27 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(default='Class', max_length=50),
        ),
    ]
