# Generated by Django 3.1.7 on 2021-03-09 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210306_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_set',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
