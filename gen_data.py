from ballons import *

import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--nb_players", required=False, help="number of players [2, 3, 4, 5]", default=2, type=int)
ap.add_argument("-p", "--nb_parents", required=False, help="number of parent cards [0, 1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-b", "--nb_balloons", required=False, help="number of balloons per player [1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-i", "--nb_iterations", required=False, help="number of iterations", default=10, type=int)
args = vars(ap.parse_args())

for i in range(args["nb_iterations"]):
	game = BalloonGame(args["nb_players"], args["nb_balloons"], args["nb_parents"])
	print(game.run_game())