
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

def gen41():
	hands = []
	for c4 in colors():
		for c1 in colors()-set([c4]):
			hands.append([c4]*4 + [c1])
	return hands

def gen32():
	hands = []
	for c3 in colors():
		for c2 in colors()-set([c3]):
			hands.append([c3]*3 + [c2]*2)
	return hands

def gen311():
	pass

def gen221():
	pass

def gen2111():
	pass


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