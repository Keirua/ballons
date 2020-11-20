
RED = 0
BLUE = 1
GREEN = 2
YELLOW = 3
PURPLE = 4

def colors():
	return set([RED, BLUE, GREEN, YELLOW, PURPLE])
 

# So we have 7 kind of hands, and we need to generate every possible hand for all of them

def gen11111():
	return [colors()]

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

def hand_to_str(hand):
	out = ""
	mapping = {
		RED: "R",
		BLUE: "B",
		GREEN: "G",
		YELLOW: "Y",
		PURPLE: "P"
	}

	for c in hand:
		out += mapping[c]
	return out

def dump_hands(hand_name, hands):
	with open("data2/hands/{}.txt".format(hand_name), 'w') as f:
		for item in hands:
			f.write("%s\n" % hand_to_str(item))

def is_valid_encounter(h1, h2):
	colors = {
		RED: 0,
		BLUE: 0,
		GREEN: 0,
		YELLOW: 0,
		PURPLE: 0,
	}
	for c in h1:
		colors[c] += 1
	for c in h2:
		colors[c] += 1
	for c in colors():
		if colors[c] > 5:
			return False
	return True

hands = {
	"11111": gen11111(),
	"5": gen5(),
	"41": gen41(),
	"32": gen32(),
	"311": gen311(),
	"221": gen221(),
	"2111": gen2111()
}

for hand in hands.keys():
	print("{}\t{}".format(hand, len(hands[hand])))
	dump_hands(hand, hands[hand])