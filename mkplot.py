import argparse
import os
import matplotlib.pyplot as plt

def read_file_data(file_name: str) -> list:
    text_data = list()
    if os.path.exists(file_name):
        open_file = open(file_name, 'r')
        text_data = open_file.readlines()
        text_data = list(filter(None, text_data))
    return list(map(int, text_data))

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True, help="The file for which to generate a plot")
args = vars(ap.parse_args())

data = read_file_data(args["file"])

file_without_extension = os.path.splitext(args["file"])[0]
output_diagram_file = "{}.png".format(file_without_extension)

plt.hist(data, bins=list(range(4, 100)))
# plt.show()
plt.savefig(output_diagram_file)