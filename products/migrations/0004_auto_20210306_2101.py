# Generated by Django 3.1.7 on 2021-03-07 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comtent',
            new_name='content',
        ),
    ]
