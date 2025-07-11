# Generated by Django 5.2.3 on 2025-06-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_gamescore_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='wyr_impulsive_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='wyr_moderate_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='wyr_too_slow_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='game_name',
            field=models.CharField(choices=[('RTT', 'RTT'), ('FC', 'FC'), ('BART', 'BART'), ('CAN', 'CAN'), ('STROOP', 'STROOP'), ('WYR', 'WYR')], max_length=50),
        ),
    ]
