# Generated by Django 4.2 on 2023-06-17 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0002_remove_advertisement_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
