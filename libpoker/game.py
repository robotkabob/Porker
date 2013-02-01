import deck
import hand
import card


class Game():
	def __init__(self, players):
		self.deck = deck.Deck()
		self.hands = []
		for i in range(players):
			self.hands.append(hand.Hand())

