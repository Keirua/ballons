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

files = [
	'data/2-2-5-1000000.dat',
	'data/2-3-5-1000000.dat',
	'data/2-4-5-1000000.dat',
	'data/2-5-5-1000000.dat',
]

data = [read_file_data(f) for f in files]

fig, axs = plt.subplots(len(files), sharex=True, sharey=True)
fig.suptitle('{} histogram comparison'.format(len(files)))

for i in range(len(files)):
	axs[i].hist(data[i], bins=list(range(4, 100)))
	axs[i].set_title(files[i])

output_diagram_file = "data/stacked{}.png".format(len(files))
plt.savefig(output_diagram_file)