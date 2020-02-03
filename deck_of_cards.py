# Deck of Cards Exercise Introduction Text
# OOP Exercise

# Introduction

# Your goal in this exercise is to implement two classes, Card  and Deck .

# Specifications

# Card 

#     Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
#     Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
#     Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

# Deck 

#     Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
#     Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
#     Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
#     Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
#     Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
#     Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
#     Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
    	return str(self.value) + " of " + str(self.suit)

class Deck:
    def __init__(self):
      suits = ("Hearts", "Diamonds", "Clubs", "Spades")
      values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
      self.cards = [Card(v, s) for s in suits for v in values]
      # for s in suits:
      #   for v in values:
      #       self.cards.append(Card(v,s))
    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def __iter__(self):
        return iter(self.cards)
    
    def reset(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(v, s) for s in suits for v in values]


    def count(self):
        return len(self.cards)

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError('All cards have been dealt')
        actual = min([num, self.count()])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self.cards.pop()

    def deal_hand(self, num):
      return self._deal(num)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('All cards have been dealt')
        shuffle(self.cards)
        shuffle(self.cards)
        shuffle(self.cards)
        shuffle(self.cards)
        shuffle(self.cards)
        return self

# d = Deck()
# for c in d:
#     print c