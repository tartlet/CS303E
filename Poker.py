# File: Poker.py
# Student: Jingsi Zhou
# UT EID: jz24729
# Course Name: CS303E
# Unique Number: 50695
# 
# Date Created: 12/01/2020
# Date Last Modified: 12/01/2020
# Description of Program: Draws a given amount of hands from a shuffled deck and outputs the evaluation of a hand. 
# If the number of cards in a deck are exhausted, a new shuffled deck is created to continue drawing. Code for
# Card, Deck, and Hand was taken from the slidesets. Also, this code is kinda bad. :D


import Card
import Deck
from Hand import *
import random
def evaluateHand(r, s):
    if hasRoyalFlush(r, s):
        return "Royal Flush"
    elif hasStraightFlush(r, s):
        return "Straight Flush"
    elif hasFourOfAKind(r, s):
	    return "Four of a kind"
    elif hasFullHouse(r, s):
	    return "Full House"
    elif hasFlush(r, s):
	    return "Flush"
    elif hasStraight(r, s):
	    return "Straight"
    elif hasThreeOfAKind(r, s):
	    return "Three of a kind"
    elif hasTwoPair(r, s):
	    return "Two pair"
    elif hasPair(r, s):
	    return "One Pair"
    else:
	    return "Nothing"    
        
def hasRoyalFlush(r, s):
    if r[0] == 1 and r[9] == 1 and r[10] == 1 and r[11] == 1 and r[12] == 1 and 5 in s:
        return True
    else:
        return False
        
def hasStraightFlush(r, s):
    if hasFlush(r,s) and hasStraight(r,s):
        return True
    else:
        return False

def hasFourOfAKind(r,s):
    if 4 in r:
        return True
    else:
        return False
    
def hasFullHouse(r,s):
    if 3 in r and 2 in r:
        return True
    else:
        return False
        
def hasFlush(r, s):
    if 5 in s:
        return True
    else:
        return False
        
def hasStraight(r, s):
    for i in range(len(r)-1):
        for j in range(5):
            if r[j] != 1:
                return False
    return True
    
def hasThreeOfAKind(r, s):
    if 3 in r:
        return True
    else:
        return False
        
def hasTwoPair(r, s):
    x = 0
    for i in range(len(r)-1):
        if r[i] == 2:
            x = x + 1
    if x == 2:
        return True
    else:
        return False
        
def hasPair(r, s):
    if 2 in r:
        return True
    else:
        return False
        
numHands = int(input("How many hands should I deal? "))
d = Deck()
d.shuffle()
for i in range(1, numHands+1):
    mysuits = [0] * 4
    myranks = [0] * 13
    if len(d) < 5:
        print("Dealing a new deck.")
        print()
        d = Deck()
        d.shuffle()
    print("Hand drawn (", i, "):")
    hand = Hand(d)
    print(hand)
    for i in range(5):
        if hand.getCard(i).getSuit() == "Spades":
            mysuits[0] = mysuits[0] + 1
        elif hand.getCard(i).getSuit() == "Diamonds":
            mysuits[1] = mysuits[1] + 1
        elif hand.getCard(i).getSuit() == "Hearts":
            mysuits[2] = mysuits[2] + 1
        else:
            mysuits[3] = mysuits[3] + 1
            
        if hand.getCard(i).getRank() == "Ace":
            myranks[0] = myranks[0] + 1
        elif hand.getCard(i).getRank() == "2":
            myranks[1] = myranks[1] + 1
        elif hand.getCard(i).getRank() == "3":
            myranks[2] = myranks[2] + 1
        elif hand.getCard(i).getRank() == "4":
            myranks[3] = myranks[3] + 1
        elif hand.getCard(i).getRank() == "5":
            myranks[4] = myranks[4] + 1
        elif hand.getCard(i).getRank() == "6":
            myranks[5] = myranks[5] + 1
        elif hand.getCard(i).getRank() == "7":
            myranks[6] = myranks[6] + 1
        elif hand.getCard(i).getRank() == "8":
            myranks[7] = myranks[7] + 1
        elif hand.getCard(i).getRank() == "9":
            myranks[8] = myranks[8] + 1
        elif hand.getCard(i).getRank() == "10":
            myranks[9] = myranks[9] + 1
        elif hand.getCard(i).getRank() == "Jack":
            myranks[10] = myranks[10] + 1
        elif hand.getCard(i).getRank() == "Queen":
            myranks[11] = myranks[11] + 1
        else: 
            myranks[12] = myranks[12] + 1
    print(evaluateHand(myranks, mysuits))
    print()

   