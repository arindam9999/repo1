# Generated by Django 2.2.2 on 2019-06-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_hotel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='date_of_booking',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clientrequest',
            name='time_of_booking',
            field=models.CharField(max_length=100),
        ),
    ]
