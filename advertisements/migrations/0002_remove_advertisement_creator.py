# Generated by Django 4.2 on 2023-06-17 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='creator',
        ),
    ]
