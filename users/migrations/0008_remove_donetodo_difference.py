# Generated by Django 3.1.3 on 2021-01-08 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210107_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donetodo',
            name='difference',
        ),
    ]
