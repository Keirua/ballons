from ballons import *
from hands_lib import *

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

def dump_encounters(encounter_name, encounters):
	with open("data2/valid-encounters/{}.txt".format(encounter_name), 'w') as f:
		for h1, h2 in encounters:
			f.write("%s-%s\n" % (hand_to_str(h1), (hand_to_str(h2))))

hands = {
	"11111": gen11111(),
	"5": gen5(),
	"41": gen41(),
	"32": gen32(),
	"311": gen311(),
	"221": gen221(),
	"2111": gen2111()
}

def generate_valid_encounters(hands1, hands2):
	valid_encounters = []
	for h1 in hands[hand1]:
		for h2 in hands[hand2]:
			if is_valid_encounter(h1, h2):
				valid_encounters.append([h1, h2])
	return valid_encounters

for hand in hands.keys():
	print("{}\t{}".format(hand, len(hands[hand])))
	dump_hands(hand, hands[hand])


for hand1 in hands.keys():
	for hand2 in hands.keys():
		valid_encounters = generate_valid_encounters(hands[hand1], hands[hand2])
		dump_encounters("{}-{}".format(hand1, hand2), valid_encounters)