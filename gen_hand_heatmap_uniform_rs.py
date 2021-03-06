from ballons import *
from hands_lib import *
from random import choice

import argparse

from cffi import FFI
ffi = FFI()
ffi.cdef("""
    bool run_game_with_known_hand(unsigned int* hand1, unsigned int* hand2, unsigned int length);
""")

C = ffi.dlopen("./ballonslib/target/release/libballonslib.so")

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--nb_parents", required=False, help="number of parent cards [0, 1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-b", "--nb_balloons", required=False, help="number of balloons per player [1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-i", "--nb_iterations", required=False, help="number of iterations", default=10, type=int)
args = vars(ap.parse_args())

hands_structure = [
   "11111",
   "5",
   "41",
   "32",
   "311",
   "221",
   "2111"
]
counts = {}
for hand0 in hands_structure:
	counts[hand0] = {}
	for hand1 in hands_structure:
		counts[hand0][hand1] = [0, 0]
# import pickle
# counts = pickle.load(open("notes/results.p", "rb"))

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

for hand1 in hands.keys():
	for hand2 in hands.keys():
		if counts[hand1][hand2][0] > args["nb_iterations"]:
			continue

		valid_encounters = generate_valid_encounters(hands[hand1], hands[hand2])

		if len(valid_encounters) > 0:
			for i in range(args["nb_iterations"]):
				# pick a random hand, an run a game with this
				encounter = choice(valid_encounters)

				counts[hand1][hand2][1] += 1 # the total count of such encounters we faced
				# print(encounter[0])
				# print(encounter[1])
				if C.run_game_with_known_hand(encounter[0], encounter[1], 5):
					counts[hand1][hand2][0] += 1 # how many times player 0 won (since player 1 lost)

print(counts)