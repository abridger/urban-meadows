# Generated by Django 2.1.7 on 2019-02-15 17:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meadows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meadow',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='meadow',
            name='updated_by',
            field=models.ManyToManyField(related_name='meadows_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
