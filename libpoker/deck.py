import card
import random


#
# The "top" card on the deck is the last card in self.cards. Use pop to draw the top card.
#

class Deck():
	def __init__(self):
		self.cards = []
		self.outCards = []	#for popped cards
		for s in card.suits:
			for v in card.values:
				self.cards.append(   card.Card(v,s)   ) 

	def shuffle(self):
		random.shuffle(self.cards)

	def pop(self):
		"""Removes and returns top card on the deck."""
		self.outCards.append(self.cards[-1])
		return self.cards.pop()


