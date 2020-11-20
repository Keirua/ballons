from ballons import *

def colors():
	return set([RED, BLUE, GREEN, YELLOW, PURPLE])

# So we have 7 kind of hands, and we need to generate every possible hand for all of them

def gen11111():
	return [[c for c in colors()]]

def gen5():
	hands = [ [c]*5 for c in colors()]
	return hands

def gen_two_colors_hand(nb_c1, nb_c2):
	hands = []
	for c1 in colors():
		for c2 in colors()-set([c1]):
			hands.append([c1]*nb_c1 + [c2]*nb_c2)
	return hands

def gen41():
	return gen_two_colors_hand(4, 1)

def gen32():
	return gen_two_colors_hand(3, 2)

def gen_three_colors_hand(nb_c1, nb_c2, nb_c3):
	hands = []
	for c1 in colors():
		for c2 in colors()-set([c1]):
			for c3 in colors()-set([c1])-set([c2]):
				hands.append([c1]*nb_c1 + [c2]*nb_c2 + [c3]*nb_c3)
	return hands

def gen311():
	return gen_three_colors_hand(3, 1, 1)

def gen221():
	return gen_three_colors_hand(2, 2, 1)

def gen2111():
	hands = []
	for c1 in colors():
		for c2 in colors()-set([c1]):
			for c3 in colors()-set([c1])-set([c2]):
				for c4 in colors()-set([c1])-set([c2])-set([c3]):
					hands.append([c1]*2 + [c2, c3, c4])
	return hands

def is_valid_encounter(h1, h2):
	counts = {
		RED: 0,
		BLUE: 0,
		GREEN: 0,
		YELLOW: 0,
		PURPLE: 0,
	}
	for c in list(h1):
		counts[c] += 1
	for c in list(h2):
		counts[c] += 1
	for c in [RED, BLUE, GREEN, YELLOW, PURPLE]:
		if counts[c] > 5:
			return False
	return True
