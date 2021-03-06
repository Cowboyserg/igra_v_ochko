from main import Card
from random import shuffle
class Deck(object):
    def __init__(self):
        # ранги
        ranks = "23456789TJQKA"
        # масти
        suits = "DCHS"
        # генератор списков создающий колоду из 52 карт
        self.cards = [Card(r, s) for r in ranks for s in suits]
        # перетасовываем колоду. Не забудьте импортировать функцию shuffle из модуля random
        shuffle(self.cards)

    def deal_card(self):
        """ Функция сдачи карты """
        return self.cards.pop()
