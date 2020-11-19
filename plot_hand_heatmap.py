
import numpy as np

data = {'1112': {'1112': [1096634, 2264360], '122': [534765, 1316073], '113': [199703, 633220], '11111': [169968, 292299], '23': [43289, 163734], '14': [5431, 37203], '5': [7, 314]}, '122': {'1112': [748418, 1317176], '122': [387001, 793237], '113': [159508, 408524], '11111': [108201, 163988], '23': [36298, 109777], '14': [5929, 30139], '5': [30, 379]}, '113': {'1112': [420634, 632480], '122': [242647, 409511], '113': [106885, 217067], '11111': [54222, 72753], '23': [26445, 61486], '14': [4603, 16608], '5': [21, 175]}, '11111': {'1112': [112353, 292343], '122': [51235, 163561], '113': [17070, 72373], '11111': [18536, 38556], '23': [3447, 18062], '14': [292, 2964], '5': [0, 0]}, '23': {'1112': [118097, 163429], '122': [71744, 109826], '113': [34123, 61269], '11111': [14407, 18205], '23': [9059, 18273], '14': [1761, 5487], '5': [11, 75]}, '14': {'1112': [31439, 37283], '122': [24018, 30261], '113': [11879, 16574], '11111': [2688, 3042], '23': [3644, 5433], '14': [765, 1513], '5': [6, 25]}, '5': {'1112': [306, 318], '122': [318, 344], '113': [170, 184], '11111': [0, 0], '23': [69, 80], '14': [15, 17], '5': [0, 0]}}

interesting_hands = ['1112', '122', '113', '11111', '23']
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