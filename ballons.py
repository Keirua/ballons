from random import *
import json 

# The five kind of balloons
RED = 0
BLUE = 1
GREEN = 2
YELLOW = 3
PURPLE = 4
# Action card that recovers a balloon
PARENT = 5


class Player:
	def __init__(self):
		self.balloons = {}
		self.bursted_balloons = []
		self.nb_balloons = 0
		self.remaining_cards = {}

		for v in [RED, BLUE, GREEN, YELLOW, PURPLE]:
			self.balloons[v] = 0
		
		self.reset_memory_of_remaining_cards()

	def reset_memory_of_remaining_cards(self):
		for v in [RED, BLUE, GREEN, YELLOW, PURPLE]:
			self.remaining_cards[v] = 4

		self.remaining_cards[PARENT] = 5

	def deal_hand(self, hand):
		for b in hand:
			self.deal_balloon(b)

	def deal_balloon(self, balloon):
		self.balloons[balloon] += 1
		self.nb_balloons += 1

	def play_action_card(self, action):
		if action == PARENT:
			self.recover_balloon()
		else:
			self.burst_ballon(action)

	def recover_balloon(self):
		# random play: among the bursted balloons, we randomly recover one
		shuffle(self.bursted_balloons)
		if len(self.bursted_balloons) > 0:
			balloon = self.bursted_balloons.pop()
			self.balloons[balloon] += 1

	def notify(self, action_card):
		self.remaining_cards[action_card] -= 1

	def burst_ballon(self, balloon):
		if self.balloons[balloon] > 0:
			self.balloons[balloon] -= 1
			self.bursted_balloons.append(balloon)

	def has_lost(self):
		return len(self.bursted_balloons) == self.nb_balloons

	def hand_structure(self):
		counts = sorted(self.balloons.values())
		counts = filter(lambda item: item != 0, counts)
		return "".join(map(str, counts))

	def __repr__(self):
		return json.dumps(self.balloons)


class CounterPlayer(Player):
	def recover_balloon(self):
		nb_burst_balloons = len(self.bursted_balloons)
		if nb_burst_balloons > 0:
			# if we have more than one bursted balloon, maybe we can improve our odds ?
			if nb_burst_balloons > 1:
				# simple heuristic: if we want to stay longer in game, among all the bursted balloons we have,
				# we simply recover the one that has the least cards remaining in the deck
				best_count = 6
				best_balloon = None
				for b in self.bursted_balloons:
					if self.remaining_cards[b] < best_count:
						best_count = self.remaining_cards[b]
						best_balloon = b
				self.bursted_balloons.remove(best_balloon)
				self.balloons[best_balloon] += 1
			else:
				balloon = self.bursted_balloons.pop()
				self.balloons[balloon] += 1


	def __repr__(self):
		return json.dumps(self.balloons)

class BalloonGame:
	def __init__(self, nb_players, nb_cards_per_player = 5, nb_parent_cards = 5):
		self.nb_players = nb_players
		self.nb_cards_per_player = nb_cards_per_player
		self.nb_parent_cards = nb_parent_cards
		self.create_game(nb_players, nb_cards_per_player, nb_parent_cards)


	def create_game(self, nb_players, nb_cards_per_player, nb_parent_cards):
		# Create a random action deck with
		self.actions = self.generate_actions_deck(nb_parent_cards)
		deck = self.generate_balloon_deck()

		# Create nb players with random balloonss
		self.players = [Player() for p in range(nb_players)]
		for c in range(nb_cards_per_player):
			for p in range(nb_players):
				self.players[p].deal_balloon(deck.pop())

		# pick a random first player
		self.current_player = 0 # chosen with fair dice

	def create_2_player_game_with_known_hands(hand1, hand2):
		game = BalloonGame(2, 5, 5)

		# override hands with custom selection
		game.players = [Player() for p in range(2)]
		game.players[0].deal_hand(hand1)
		game.players[1].deal_hand(hand2)
		return game

	def generate_balloon_deck(self):
		deck = []

		for v in [RED, BLUE, GREEN, YELLOW, PURPLE]:
			for i in range(0, 5):
				deck.append(v)

		shuffle(deck)
		return deck

	def generate_actions_deck(self, nb_parent_cards = 5):
		actions = []

		for v in [RED, BLUE, GREEN, YELLOW, PURPLE]:
			for i in range(0, 4):
				actions.append(v)

		for i in range(0, nb_parent_cards):
			actions.append(PARENT)

		shuffle(actions)
		return actions

	def play_action_card(self):
		action = self.pick_action_card()
		self.players[self.current_player].play_action_card(action)
		for p in self.players:
				p.notify(action)
		if self.players[self.current_player].has_lost():
			return False
		else:
			self.change_player()
			return True

	def pick_action_card(self):
		action = self.actions.pop()
		if len(self.actions) == 0:
			self.actions = self.generate_actions_deck(self.nb_parent_cards)
			for p in self.players:
				p.reset_memory_of_remaining_cards()
		return action

	def change_player(self):
		self.current_player = (self.current_player + 1) % self.nb_players

	def run_game(self):
		nb_cards_played = 0
		while self.play_action_card():
			nb_cards_played += 1

		return nb_cards_played

	def __repr__(self):
		return "\n".join(["{}".format(p) for p in self.players])

class BalloonGameWithKnownHands(BalloonGame):
	def __init__(self, hand1, hand2):
		self.nb_players = 2
		self.nb_cards_per_player = 5
		self.nb_parent_cards = 5
		# Create a random action deck with
		self.actions = self.generate_actions_deck(self.nb_parent_cards)
		deck = self.generate_balloon_deck()

		# override hands with custom selection
		self.players = [Player() for p in range(2)]
		self.players[0].deal_hand(hand1)
		self.players[1].deal_hand(hand2)

		# pick a random first player
		self.current_player = 0 # chosen with fair dice


class BalloonGameWithKnownHandsAndCounter(BalloonGame):
	def __init__(self, hand1, hand2):
		self.nb_players = 2
		self.nb_cards_per_player = 5
		self.nb_parent_cards = 5
		# Create a random action deck with
		self.actions = self.generate_actions_deck(self.nb_parent_cards)
		deck = self.generate_balloon_deck()

		# override hands with custom selection
		self.players = [CounterPlayer(), Player()]
		self.players[0].deal_hand(hand1)
		self.players[1].deal_hand(hand2)

		# pick a random first player
		self.current_player = 0 # chosen with fair dice
