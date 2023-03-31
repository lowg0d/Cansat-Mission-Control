import matplotlib.pyplot as plt

# read data from file
with open('./saves_good/LOG.TXT', 'r') as f:
    data = f.read().strip().split('\n')

# separate y values and plot
y_values = []
for line in data:
    values = line.split(';')
    if len(values) > 1:
        y = float(values[0])  # use first value as y-value
        y_values.append(y)

plt.plot([1]*len(y_values), y_values)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('My Plot')
plt.show()
