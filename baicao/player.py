class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def hello(self):
        print("Hello, my name is", self.name)