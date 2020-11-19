from ballons import *

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--nb_parents", required=False, help="number of parent cards [0, 1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-b", "--nb_balloons", required=False, help="number of balloons per player [1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-i", "--nb_iterations", required=False, help="number of iterations", default=10, type=int)
args = vars(ap.parse_args())


counts = {}
for i in range(args["nb_iterations"]):
	game = BalloonGame(1, args["nb_balloons"], args["nb_parents"])
	key = game.players[0].hand_structure()
	if key in counts:
		counts[key] += 1
	else:
		counts[key] = 1

print({k: v for k, v in sorted(counts.items(), key=lambda item: item[1])})

# most frequent hands:
# '1112', '122', '113', '11111', '23', '14', '5'
# raw hand count with 1000000 hands:
# {'5': 100, '14': 9426, '23': 37340, '11111': 58588, '113': 141093, '122': 283629, '1112': 469824}
# {'5': 94,  '14': 9519, '23': 37610, '11111': 59149, '113': 141198, '122': 281279, '1112': 471151}
# problem = quadratic convergence: having 1 more digit = 100 times more iterations
# time python3 gen_hand_structure.py -p 5 -b 5 -i 1000000
# {'5': 79, '14': 9387, '23': 37784, '11111': 58973, '113': 140978, '122': 282434, '1112': 470365}
# 
# real	0m19,588s
# user	0m19,587s
# sys	0m0,000s