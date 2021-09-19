import random
from Card import *

class Deck :
    def __init__(self):
        self.__cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                c = Card(rank, suit)
                self.__cards.append(c)
    def shuffle(self):
        random.shuffle(self.__cards)
    def deal(self ):
        if len(self) == 0:
            return None
        else :
            return self.__cards.pop(0)
    def __len__ (self):
        return len(self.__cards)
    def __len__(self):
        return len(self.__cards)
    def __str__(self):
        result = ""
        for c in self.__cards :
            result = result + str (c) + "\n"
        return result