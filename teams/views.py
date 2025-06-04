from datetime import datetime
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
# Create your views here.


class TeamsViews(APIView):
    def get(self, request):
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            t = model_to_dict(team)
            teams_list.append(t)

        return Response(teams_list, 200)

    def post(self, request):
        team_data = request.data

        if team_data["titles"] < 0:
            return Response({"error": "titles cannot be negative"}, 400)

        first_cup_object = datetime.strptime(team_data["first_cup"], "%Y-%m-%d")
        year = int(first_cup_object.strftime("%Y")) - 1930
        if year % 4 != 0:
            return Response({"error": "there was no world cup this year"}, 400)

        now = datetime.now()
        cup_qtd_now = round((int(now.strftime("%Y")) - 1930) / 4, 1)
        cup_qtd_selecao = round(cup_qtd_now - round((year / 4), 1), 0)
        if team_data["titles"] > cup_qtd_selecao:
            return Response({"error": "impossible to have more titles than disputed cups"}, 400)

        team = Team.objects.create(**team_data)

        return Response(model_to_dict(team), 201)


class TeamsViewsDetails(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        return Response(model_to_dict(team))

    def patch(self, request, team_id):
        team_data = request.data
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        for keys in ["name", "titles", "top_scorer", "fifa_code", "first_cup"]:
            if keys in team_data:
                setattr(team, keys, team_data[keys])
        team.save()

        return Response(model_to_dict(team), 200)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)
        team.delete()

        return Response({}, 204)
