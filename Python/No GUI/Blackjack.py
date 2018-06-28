import random

def deal(deck):
	card = random.choice(deck)
	deck.remove(card)
	return card

def playBlackjack():
	players = [AI('Stardust'), Manual('Manual')]
	deck_count = 1
	
	scores = [0 for _ in players]
	deck = ['A','K','Q','J',10,9,8,7,6,5,4,3,2] * 4 * deck_count
	faceUp = deal(deck)
	dealt = [faceUp]
	for id, player in enumerate(players):
		hand = Hand([deal(deck), deal(deck)])
		dealt.extend(hand)
		while hand.value() <= 21:
			if player.choice(hand, faceUp, dealt):
				card = deal(deck)
				dealt.append(card)
				hand.addCard(card)
			else:
				break # If player chooses to stay, stop dealing
		finalVal = hand.value()
		scores[id] = finalVal
	faceDown = deal(deck)
	dealer = Hand([faceUp,faceDown])
	while dealer.value() < 17 or dealer.value(1) == (17,1):
		dealer.addCard(deal(deck))
	finalDealer = dealer.value() 
	if finalDealer > 21:
		print('Dealer busted with {}!'.format(finalDealer))
	elif finalDealer == 21:
		print("Dealer got a blackjack!")
	else:
		print("Dealer scored {}.".format(finalDealer))
	for id, player in enumerate(players):
		score = scores[id]
		if score > 21:
			print('{} busted with {}.'.format(player.name,score))
		elif score == 21:
			print('{} got a blackjack!'.format(player.name,score))
		else:
			if score > finalDealer or finalDealer > 21:
				status = 'won'
			elif score == finalDealer:
				status = 'tied'
			else:
				status = 'lost'
			print("{} scored {} and {}.".format(player.name,score,status))
	print('\n\n')

class Hand():
	def __init__(self, cards):
		self.cards = []
		for card in cards:
			self.addCard(card)

	def __iter__(self):
		return iter(self.cards)
			
	def addCard(self, card):
		self.cards.append(card)
		
	def value(self, dealer = 0):
		val = 0
		aceCount = 0
		soft = 0
		for card in self.cards:
			if card == 'A':
				aceCount += 1
				val += 1
			elif type(card) == str:
				val += 10
			elif type(card) == int:
				val += card
		for ace in range(aceCount):
			if val <= 11:
				soft = 1
				val += 10
			else:
				break
		if dealer:
			return val, soft
		else:
			return val
			

class Player():
	def __init__(self, name):
		self.name = name
		
class AI(Player):
	def choice(self, hand, faceUp, dealt): # Returns whether to hit (1) or stay (0) on a given hand
		if hand.value() < 19:
			return 1
		else:
			return 0

class Manual(Player):
	def choice(self, hand, faceUp, dealt):
		return int(input('Hit (1) or stay (0) with hand of {}?\n'.format(hand.cards)))

		
while 1: playBlackjack()
