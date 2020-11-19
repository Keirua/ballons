import argparse
import os
import matplotlib.pyplot as plt

import json
import ast
import collections
import numpy as np

def read_file_data(filename):
  with open(filename, "r") as f:
    contents = f.read()
    data = ast.literal_eval(contents)

    sorted_data = [0 for i in range(0, 300)]
    for k in data.keys():
    	if k < 300:
    		sorted_data[k] = data[k]
    total = sum(sorted_data)

    sorted_data = [sorted_data[i] for i in range(len(sorted_data))]
    return sorted_data



ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="The file for which to generate a plot")
args = vars(ap.parse_args())

data = read_file_data(args["file"])

print(data)
file_without_extension = os.path.splitext(args["file"])[0]
output_diagram_file = "{}.png".format(file_without_extension)

plt.bar(range(5, 100), data[5:100])
plt.show()
plt.savefig(output_diagram_file)