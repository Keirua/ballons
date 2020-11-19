import matplotlib.pyplot as plt

data = {'5': 79, '14': 9387, '23': 37784, '11111': 58973, '113': 140978, '122': 282434, '1112': 470365}

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = data.keys()
sizes = data.values()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, pctdistance=0.9, labeldistance=1.1)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('data2/piechart.png')

total = sum(sizes)

for l in labels:
	d = data[l]
	print("{}, {}".format(l, 100*d/total))