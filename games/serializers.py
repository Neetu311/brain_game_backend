# games/serializers.py

from rest_framework import serializers
from .models import GameScore

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        # Add 'participant_email' here
        fields = [
            'id', 'participant_email', 'game_name', 'rtt_average_reaction_time', 'rtt_total_rounds',
            'flanker_accuracy', 'flanker_correct_count', 'flanker_total_rounds', 'flanker_avg_reaction_time',
            'bart_total_cash', 'bart_avg_pumps', 'bart_unpopped_balloons', 'bart_pumps_on_unpopped_balloons',
            'can_final_time', 'can_total_elements',
            'stroop_correct_congruent', 'stroop_correct_incongruent', 'stroop_total_congruent', 'stroop_total_incongruent',
            'stroop_avg_rt_congruent', 'stroop_avg_rt_incongruent',
            'wyr_impulsive_count', 'wyr_moderate_count', 'wyr_too_slow_count',
            'timestamp', 'raw_game_data'
        ]
        read_only_fields = ['id', 'timestamp'] # These fields are typically set by the server