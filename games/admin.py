from django.contrib import admin
from django.utils import timezone
from .models import GameScore

@admin.register(GameScore)
class GameScoreAdmin(admin.ModelAdmin):
    list_display = (
        'game_name', 'participant_email', 'formatted_timestamp',
        'rtt_average_reaction_time', 
        'flanker_accuracy',           # This will show your Flanker accuracy
        'flanker_avg_reaction_time',  # This will show your Flanker reaction time  
        'bart_total_cash',
        'can_final_time',
        'wyr_impulsive_count', 'wyr_moderate_count', 'wyr_too_slow_count',
        'stroop_avg_rt_incongruent',
        'stroop_avg_rt_congruent',
    )
    
    fieldsets = (
        (None, {
            'fields': ('participant_email', 'game_name', 'raw_game_data')
        }),
        ('RTT Data', {
            'fields': ('rtt_average_reaction_time', 'rtt_total_rounds'),
            'classes': ('collapse',)
        }),
        ('Flanker Challenge Data', {
            'fields': ('flanker_accuracy', 'flanker_correct_count', 'flanker_total_rounds', 'flanker_avg_reaction_time'),
            'classes': ('collapse',)
        }),
        ('BART Data', {
            'fields': ('bart_total_cash', 'bart_avg_pumps', 'bart_unpopped_balloons', 'bart_pumps_on_unpopped_balloons'),
            'classes': ('collapse',)
        }),
        ('CAN Data', {
            'fields': ('can_final_time', 'can_total_elements'),
            'classes': ('collapse',)
        }),
        ('STROOP Data', {
            'fields': (
                'stroop_correct_congruent', 'stroop_correct_incongruent',
                'stroop_total_congruent', 'stroop_total_incongruent',
                'stroop_avg_rt_congruent', 'stroop_avg_rt_incongruent'
            ),
            'classes': ('collapse',)
        }),
        ('Would You Rather Data', {
            'fields': ('wyr_impulsive_count', 'wyr_moderate_count', 'wyr_too_slow_count'),
            'classes': ('collapse',)
        }),
    )
    
    list_filter = ('game_name', 'timestamp')
    search_fields = ('game_name', 'participant_email')

    def formatted_timestamp(self, obj):
        if obj.timestamp:
            local_time = timezone.localtime(obj.timestamp)
            return local_time.strftime('%b %d, %Y, %H:%M')
        return "No timestamp"
    
    formatted_timestamp.short_description = 'Timestamp (Local)'
    formatted_timestamp.admin_order_field = 'timestamp'