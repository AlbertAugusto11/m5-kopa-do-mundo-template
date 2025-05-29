# "titles cannot be negative"
class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


# "there was no world cup this year"
class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


# "impossible to have more titles than disputed cups"
class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message
