import numpy as np
import pickle

# data = pickle.load(open("notes/results.p", "rb"))
# data with the rust implementation of random play
data_default = {'11111': {'11111': [47717, 100000], '5': [0, 0], '41': [10470, 100000], '32': [19045, 100000], '311': [22469, 100000], '221': [30415, 100000], '2111': [37516, 100000]}, '5': {'11111': [0, 0], '5': [49962, 100000], '41': [75715, 100000], '32': [86602, 100000], '311': [88586, 100000], '221': [92827, 100000], '2111': [95045, 100000]}, '41': {'11111': [88793, 100000], '5': [23996, 100000], '41': [49737, 100000], '32': [66697, 100000], '311': [70526, 100000], '221': [79542, 100000], '2111': [84292, 100000]}, '32': {'11111': [79415, 100000], '5': [13231, 100000], '41': [32596, 100000], '32': [49590, 100000], '311': [54352, 100000], '221': [64268, 100000], '2111': [71442, 100000]}, '311': {'11111': [75366, 100000], '5': [10967, 100000], '41': [28740, 100000], '32': [44613, 100000], '311': [49328, 100000], '221': [59507, 100000], '2111': [66636, 100000]}, '221': {'11111': [66348, 100000], '5': [6770, 100000], '41': [19502, 100000], '32': [33529, 100000], '311': [38470, 100000], '221': [48903, 100000], '2111': [56727, 100000]}, '2111': {'11111': [58909, 100000], '5': [4856, 100000], '41': [15418, 100000], '32': [27192, 100000], '311': [31425, 100000], '221': [40904, 100000], '2111': [48065, 100000]}}
# data with the player that counts cards
data_count = {'11111': {'11111': [5304, 10000], '5': [0, 0], '41': [1338, 10000], '32': [2379, 10000], '311': [2804, 10000], '221': [3656, 10000], '2111': [4356, 10000]}, '5': {'11111': [0, 0], '5': [4998, 10000], '41': [7717, 10000], '32': [8681, 10000], '311': [9027, 10000], '221': [9337, 10000], '2111': [9543, 10000]}, '41': {'11111': [8781, 10000], '5': [2189, 10000], '41': [4775, 10000], '32': [6572, 10000], '311': [7062, 10000], '221': [7765, 10000], '2111': [8348, 10000]}, '32': {'11111': [7915, 10000], '5': [1346, 10000], '41': [3489, 10000], '32': [5082, 10000], '311': [5684, 10000], '221': [6601, 10000], '2111': [7253, 10000]}, '311': {'11111': [7547, 10000], '5': [978, 10000], '41': [2833, 10000], '32': [4341, 10000], '311': [4938, 10000], '221': [6000, 10000], '2111': [6700, 10000]}, '221': {'11111': [6752, 10000], '5': [720, 10000], '41': [2273, 10000], '32': [3725, 10000], '311': [4176, 10000], '221': [5088, 10000], '2111': [5914, 10000]}, '2111': {'11111': [6063, 10000], '5': [543, 10000], '41': [1894, 10000], '32': [3029, 10000], '311': [3543, 10000], '221': [4461, 10000], '2111': [5169, 10000]}}

interesting_hands = ['2111', '221', '311', '11111', '32', '41', '5']
heatmap = np.zeros((len(interesting_hands), len(interesting_hands)))

for i, p0 in enumerate(interesting_hands):
	for j, p1 in enumerate(interesting_hands):

		if data_count[p0][p1][1] > 0 and data_default[p0][p1][1] > 0:
			freq_default = data_default[p0][p1][0] / float(data_default[p0][p1][1])
			freq_improved = data_count[p0][p1][0] / float(data_count[p0][p1][1])

			heatmap[i][j] = freq_improved - freq_default

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

ax.set_title("comparison of counting cards vs random play. >0 = improvement")
fig.tight_layout()
plt.show()