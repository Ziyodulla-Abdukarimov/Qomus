from django.test import TestCase


# Create your tests here.
class Monitor:
    def __init__(self, name, size, money):
        self.name = name
        self.size = size
        self.money = money

    def narxi(self):
        print(self.money)

    def malumot(self):
        print('name: ', self.name, "O'lchami: ", self.size, "Narxi: ", self.money)


class GraphicCard:
    def __init__(self, name, size, money):
        self.name = name
        self.size = size
        self.money = money

    def narxi(self):
        print(self.money)

    def malumot(self):
        print('name: ', self.name, "O'lchami: ", self.size, "Narxi: ", self.money)


monitor = Monitor('LG', 19, 1500000)
card = GraphicCard('LG', '2GB', 1500000)
monitor.narxi()
monitor.malumot()
card.narxi()
card.malumot()
