def greet(name):
    print(f"Hello, {name}")
    print(f"Howdy, {name}")
    print(f"sup, {name}?")

def print_dict():
    dict = {
    "Denver" : "Broncos",
    "Kansas": "Chiefs",
    "LA": "Chargers, Rams",
    "Tampa Bay": "Buccaneers",
    }

    return dict

class testObj:

    def __init__(self, message):
        self.text = message

    def set_message(self, message):
        self.text = message

    def get_message(self):
        return self.text
