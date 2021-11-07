

class Weather:
    APIKEY = "ba71f5ff6d30856ebd20ab63054e9e1b"

    def __init__(self, location):
        self.location = location

    def __str__(self):
        return self.location
