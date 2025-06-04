from teams.views import TeamsViews
from django.urls import path


urlpatterns = [
    path('teams/', TeamsViews.as_view())
]
