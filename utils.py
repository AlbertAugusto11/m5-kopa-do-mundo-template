from datetime import datetime
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(info_selecao: dict):
    if info_selecao["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    first_cup_object = datetime.strptime(info_selecao["first_cup"], "%Y-%m-%d")
    year = int(first_cup_object.strftime("%Y")) - 1930
    if year % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    now = datetime.now()
    cup_qtd_now = round((int(now.strftime("%Y")) - 1930) / 4, 1)
    cup_qtd_selecao = round(cup_qtd_now - round((year / 4), 1), 0)
    if info_selecao["titles"] > cup_qtd_selecao:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
