import Card
from Deck import *

class Hand:
    def __init__(self, deck):
        if (len(deck) < 5):
            print ("Not enough cards left!")
            return None
        self.__cards = []
        for i in range(5):
            card = deck.deal()
            self.__cards.append(card)
    def __str__(self):
        result = ""
        for card in self.__cards :
            result = result + str(card) + "\n"
        return result
    def getCard(self, i):
        if (0 <= i <= 4):
            return self.__cards[i]
        else:
            return None