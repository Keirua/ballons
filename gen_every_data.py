import os

nb_iterations = 1000000

for n in [2, 3, 4, 5]:
	for p in [0, 1, 2, 3, 4, 5]:
		for b in [3, 4, 5]:
			command = "python3 gen_data.py -n {} -p {} -b {} -i {} > data/{}-{}-{}-{}.dat".format(n, p, b, nb_iterations, n, p, b, nb_iterations)
			print(command)
			os.system(command)