from ballons import *

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--nb_parents", required=False, help="number of parent cards [0, 1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-b", "--nb_balloons", required=False, help="number of balloons per player [1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-i", "--nb_iterations", required=False, help="number of iterations", default=10, type=int)
args = vars(ap.parse_args())

hands = ['1112', '122', '113', '11111', '23', '14', '5']
counts = {}
for hand0 in hands:
	counts[hand0] = {}
	for hand1 in hands:
		counts[hand0][hand1] = [0, 0]

for i in range(args["nb_iterations"]):
	game = BalloonGame(2, args["nb_balloons"], args["nb_parents"])
	p0 = game.players[0].hand_structure()
	p1 = game.players[1].hand_structure()

	game.run_game()
	loser = game.current_player

	counts[p0][p1][1] += 1 # the total count of such encounters we faced
	if loser == 1:
		counts[p0][p1][0] += 1 # how many times player 0 won (since player 1 lost)

print(counts)