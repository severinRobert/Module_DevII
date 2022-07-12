import datetime

class Command():
    def __init__(self, user:int, date:datetime = datetime.datetime.now, result:dict = {}) -> None:
        self.user = user
        self.date = date
        self.result = result

    def __send_command_to_history():
        print("historique pas encore implémenté")
