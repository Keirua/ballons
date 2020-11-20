
RED = 0
BLUE = 1
GREEN = 2
YELLOW = 3
PURPLE = 4

def colors():
	return set([RED, BLUE, GREEN, YELLOW, PURPLE])
 

# So we have 7 kind of hands, 

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


print("11111")
print(gen11111())
print("")

print("5")
print(gen5())
print("")

print("41")
print(gen41())
print("")

print("32")
print(gen32())
print("")

print("311")
print(gen311())
print("")

print("221")
print(gen221())
print("")

print("2111")
print(gen2111())
print("")