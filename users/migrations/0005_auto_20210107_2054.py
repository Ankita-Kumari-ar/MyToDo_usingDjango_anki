# Generated by Django 3.1.3 on 2021-01-07 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_donetodo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DoneTodo',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]