from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import GameScore
from .serializers import GameScoreSerializer

@method_decorator(csrf_exempt, name='dispatch') # <--- MUST be here
class GameScoreViewSet(viewsets.ModelViewSet):
    queryset = GameScore.objects.all()
    serializer_class = GameScoreSerializer
    permission_classes = [AllowAny] # <--- Explicitly allows all access to this API view
                                  # even if set in settings.py, this makes it definite for THIS view.
    def perform_create(self, serializer):
        serializer.save()