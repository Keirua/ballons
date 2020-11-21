from cffi import FFI
ffi = FFI()
ffi.cdef("""
    int run_balloon_game(int, int, int);
""")

C = ffi.dlopen("./target/debug/libballons.so")

import argparse
# read the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--nb_players", required=False, help="number of players [2, 3, 4, 5]", default=2, type=int)
ap.add_argument("-p", "--nb_parents", required=False, help="number of parent cards [0, 1, 2, 3, 4, 5]", default=5, type=int)
ap.add_argument("-b", "--nb_balloons", required=False, help="number of balloons per player [1, 2, 3, 4, 5]", default=5, type=int)
args = vars(ap.parse_args())

game_length = C.run_balloon_game(args["nb_players"], args["nb_balloons"], args["nb_parents"])

print(game_length)