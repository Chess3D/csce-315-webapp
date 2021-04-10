# Generated by Django 3.2 on 2021-04-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('tournamentURL', models.CharField(max_length=255, verbose_name='TournamentURL')),
                ('tournamentDescription', models.CharField(max_length=511, verbose_name='tournamentDescription')),
                ('tournamentType', models.CharField(max_length=255, verbose_name='tournamentType')),
                ('tournamentThirdPlaceMatch', models.BooleanField(default=True, verbose_name='tournamentThirdPlaceMatch')),
                ('tournamentRankedBy', models.CharField(max_length=31, verbose_name='tournamentRankedby')),
                ('tournamentShowRounds', models.BooleanField(default=True, verbose_name='tournamentShowRounds')),
                ('tournamentPrivate', models.BooleanField(default=False, verbose_name='tournamentPrivate')),
                ('tournamentNotifyUserWhenOpen', models.BooleanField(default=False, verbose_name='tournamentNotifyUserWhenOpen')),
                ('tournamentNotifyUserWhenTournyEnd', models.BooleanField(verbose_name='tournamentNotifyUserWhenTournyEnd')),
                ('tournamentSeqPairings', models.BooleanField(default=False, verbose_name='tournamentSeqPairings')),
                ('tournamentSignUpCap', models.BigIntegerField(verbose_name='tournamentSignUpCap')),
                ('tournamentStartDate', models.DateTimeField(verbose_name='tournamentStartDate')),
                ('tournamentCheckInDuration', models.BigIntegerField(verbose_name='tournamentCheckInDuration')),
                ('tournamentGrandFinalsMod', models.CharField(max_length=31, verbose_name='tournamentGrandFinalsMod')),
                ('tournamentGameName', models.CharField(max_length=255, verbose_name='tournamentGameName')),
            ],
        ),
    ]
