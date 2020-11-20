import numpy as np
import pickle

data = pickle.load(open("notes/results.p", "rb"))

interesting_hands = ['2111', '221', '311', '11111', '32', '41', '5']
heatmap = np.zeros((len(interesting_hands), len(interesting_hands)))

for i, p0 in enumerate(interesting_hands):
	for j, p1 in enumerate(interesting_hands):
		counts = data[p0][p1]

		if counts[1] > 0:
			freq = counts[0] / float(counts[1])
			heatmap[i][j] = freq

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

ax.set_title("Frequency of wins for when a vertical hand encounters a horizontal one")
fig.tight_layout()
plt.show()