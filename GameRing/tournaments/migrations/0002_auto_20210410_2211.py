# Generated by Django 3.2 on 2021-04-10 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='tournamentCheckInDuration',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='tournamentSeqPairings',
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournamentGameName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.tournamentgame'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournamentType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.tournamenttype'),
        ),
    ]
