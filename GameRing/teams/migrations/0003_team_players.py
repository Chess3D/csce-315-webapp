# Generated by Django 3.2 on 2021-04-16 23:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0002_alter_team_elo'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
