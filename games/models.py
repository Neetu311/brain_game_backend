# games/models.py

from django.db import models
from django.utils import timezone

class GameScore(models.Model):
    # Game Choices (as defined previously)
    GAME_CHOICES = [
        ('RTT', 'RTT'),
        ('FC', 'FC'),
        ('BART', 'BART'),
        ('CAN', 'CAN'),
        ('STROOP', 'STROOP'), 
        ('WYR', 'WYR'),
    ]

    # New field for email
    participant_email = models.EmailField(max_length=255, null=True, blank=True) # Add this line

    game_name = models.CharField(max_length=50, choices=GAME_CHOICES)
    # Fields for RTT
    rtt_average_reaction_time = models.FloatField(null=True, blank=True)
    rtt_total_rounds = models.IntegerField(null=True, blank=True)

    # Fields for FC
    flanker_accuracy = models.FloatField(null=True, blank=True)
    flanker_correct_count = models.IntegerField(null=True, blank=True)
    flanker_total_rounds = models.IntegerField(null=True, blank=True)
    flanker_avg_reaction_time = models.FloatField(null=True, blank=True)

    # Fields for BART
    bart_total_cash = models.IntegerField(null=True, blank=True)
    bart_avg_pumps = models.FloatField(null=True, blank=True)
    bart_unpopped_balloons = models.IntegerField(null=True, blank=True)
    bart_pumps_on_unpopped_balloons = models.IntegerField(null=True, blank=True) # Assuming this was added

    # Fields for CAN
    can_final_time = models.FloatField(null=True, blank=True)
    can_total_elements = models.IntegerField(null=True, blank=True)

    # Fields for STROOP (will be added later for STROOP game)
    stroop_correct_congruent = models.IntegerField(null=True, blank=True)
    stroop_correct_incongruent = models.IntegerField(null=True, blank=True)
    stroop_total_congruent = models.IntegerField(null=True, blank=True)
    stroop_total_incongruent = models.IntegerField(null=True, blank=True)
    stroop_avg_rt_congruent = models.FloatField(null=True, blank=True)
    stroop_avg_rt_incongruent = models.FloatField(null=True, blank=True)

    #WYR
    wyr_impulsive_count = models.IntegerField(null=True, blank=True)
    wyr_moderate_count = models.IntegerField(null=True, blank=True)
    wyr_too_slow_count = models.IntegerField(null=True, blank=True)

    timestamp = models.DateTimeField(default=timezone.now)
    raw_game_data = models.JSONField(null=True, blank=True) # For storing full raw JSON data

    def __str__(self):
        return f"{self.game_name} Score at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"