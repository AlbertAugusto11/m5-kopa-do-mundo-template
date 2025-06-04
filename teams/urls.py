from teams.views import TeamsViews, TeamsViewsDetails
from django.urls import path


urlpatterns = [
    path('teams/', TeamsViews.as_view()),
    path('teams/<int:team_id>', TeamsViewsDetails.as_view())
]
