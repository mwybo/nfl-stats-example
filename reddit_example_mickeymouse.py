import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(size=(10))*3
y = np.random.random(size=(10))*4

labels=['team'+str(x) for x in range(10)]

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot([0, 4], [0, 4], 'k--')
for i, label in enumerate(labels):
    ax.text(x[i], y[i], labels[i])
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid()