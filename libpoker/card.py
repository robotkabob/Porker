values = [x for x in range(2,15)]
# J - 11, Q - 12, K - 13, A - 14
suits = ['c', 'd', 'h', 's' ]

class qCard():
	def __init__(self, value, suit):
		self.setValue(value)
		self.setSuit(suit)

	def setValue(self, newValue):
		"""Sets the card value. Throws an exception if invalid value given."""
		if newValue in values:

			self.value = newValue
		else:
			raise Exception("Invalid card value")

	def setSuit(self, newSuit):
		"""Sets suit value. Throws an exception if invalid value given."""
		if newSuit in suits:

			self.suit = newSuit
		else:
			raise Exception("Invalid suit")

	def getSuit(self):
		return self.suit
	def getValue(self):
		return self.value
	def getStrValue(self):
		"""Returns the value card value as a human readable string"""
		if self.value <= 10:
			return str(self.value)
		elif self.value == 11:
			return 'J'
		elif self.value == 12:
			return 'Q'
		elif self.value == 13:
			return 'K'
		elif self.value == 14:
			return 'A'
	def getStrSuit(self):
		return str(self.suit)

	def __eq__(self, other):
		if self.getValue() == other.getValue():
			if self.getSuit() == other.getSuit():
				return True
		return False

	def __str__(self):
		return self.getStrValue() + self.getStrSuit

	def generateHTML(self, style="plain"):
		"""Generates the HTML version of the card"""
		card = "card "
		rank = '<span class="rank">'
		suit = '<span class="suit">&'


		# set the card value
		if self.getValue() in range(2,11):
			htmlValue = str(self.getValue())
		else:
			htmlValue = self.getStrValue()[-1]
		card = card + "rank-" + htmlValue
		rank = rank + htmlValue + "</span>"

		# set the suit
		if self.getSuit() == 'c':
			card = card + " clubs"
			suit = suit + 'clubs;</span>'
		elif self.getSuit() == 'h':
			card = card + " hearts"
			suit = suit + 'hearts;</span>'
		elif self.getSuit() == 's':
			card = card + " spades"
			suit = suit + 'spades;</span>'
		elif self.getSuit() == 'd':
			card = card + " diams"
			suit = suit + 'diams;</span>'

		htmlClass = 'class="' + card + '"'

		if style == "plain":
			output = "<div "  + htmlClass + '>' + rank + suit + "</div>"

		return output


