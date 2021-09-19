class Card :
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__ (self, rank, suit):
        if (not rank in Card.ranks or not suit in Card.suits):
            print ("Not a legal card specification.")
            return
        self.__rank = rank
        self.__suit = suit
    def getRank(self):
        return self.__rank
    def getSuit(self):
        return self.__suit
    def __str__(self):
        return self.__rank + ' of ' + self.__suit