import numpy as np
import pickle

data = {'11111': {'11111': [47717, 100000], '5': [0, 0], '41': [10470, 100000], '32': [19045, 100000], '311': [22469, 100000], '221': [30415, 100000], '2111': [37516, 100000]}, '5': {'11111': [0, 0], '5': [49962, 100000], '41': [75715, 100000], '32': [86602, 100000], '311': [88586, 100000], '221': [92827, 100000], '2111': [95045, 100000]}, '41': {'11111': [88793, 100000], '5': [23996, 100000], '41': [49737, 100000], '32': [66697, 100000], '311': [70526, 100000], '221': [79542, 100000], '2111': [84292, 100000]}, '32': {'11111': [79415, 100000], '5': [13231, 100000], '41': [32596, 100000], '32': [49590, 100000], '311': [54352, 100000], '221': [64268, 100000], '2111': [71442, 100000]}, '311': {'11111': [75366, 100000], '5': [10967, 100000], '41': [28740, 100000], '32': [44613, 100000], '311': [49328, 100000], '221': [59507, 100000], '2111': [66636, 100000]}, '221': {'11111': [66348, 100000], '5': [6770, 100000], '41': [19502, 100000], '32': [33529, 100000], '311': [38470, 100000], '221': [48903, 100000], '2111': [56727, 100000]}, '2111': {'11111': [58909, 100000], '5': [4856, 100000], '41': [15418, 100000], '32': [27192, 100000], '311': [31425, 100000], '221': [40904, 100000], '2111': [48065, 100000]}}

interesting_hands = ['2111', '221', '311', '11111', '32', '41', '5']
heatmap = np.zeros((len(interesting_hands), len(interesting_hands)))

for i, p0 in enumerate(interesting_hands):
	for j, p1 in enumerate(interesting_hands):
		# plot the number of games that were played for a given encounter
		heatmap[i][j] = data[p0][p1][1]

import matplotlib
import matplotlib.pyplot as plt
print(heatmap)

fig, ax = plt.subplots()
im = ax.imshow(heatmap)

# We want to show all ticks...
ax.set_xticks(np.arange(len(interesting_hands)))
ax.set_yticks(np.arange(len(interesting_hands)))
# ... and label them with the respective list entries
ax.set_xticklabels(interesting_hands)
ax.set_yticklabels(interesting_hands)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(interesting_hands)):
    for j in range(len(interesting_hands)):
        text = ax.text(j, i, '%.2f' % heatmap[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Number of games that were played for each encounter")
fig.tight_layout()
plt.show()