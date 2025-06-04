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
