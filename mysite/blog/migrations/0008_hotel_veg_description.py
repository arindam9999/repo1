# Generated by Django 2.2.2 on 2019-06-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190626_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='veg_description',
            field=models.TextField(default='none'),
        ),
    ]