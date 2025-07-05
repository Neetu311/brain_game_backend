from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported
from rest_framework.routers import DefaultRouter # Import DefaultRouter
from games.views import GameScoreViewSet # Import your GameScoreViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'gamescores', GameScoreViewSet) # This sets up endpoints like /gamescores/, /gamescores/<id>/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # This line includes your API URLs
    # You can also include 'rest_framework.urls' for login/logout views for the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]