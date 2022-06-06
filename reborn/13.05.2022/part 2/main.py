import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
fig.set(facecolor = 'green')
ax.set(facecolor = 'red',
       xlim = [-10, 10],
       ylim = [-2, 2],
       title = 'Основы анатомии matplotlib',
       xlabel = 'ось абцис (XAxis)',
       ylabel = 'ось ординат (YAxis)')
plt.show()

x = [0, 1, 2, 3, 4]
y_1 = [0, 6, 7, 15, 19]
y_2 = [1, 3, 8, 12, 27]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y_1,
        color = 'black',
        linewidth = 5)
ax.scatter(x, y_2,
           color = 'blue',
           marker = '*')
plt.show()

fig = plt.figure()
ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)
ax_1.set(title = 'ax_1', xticks=[], yticks=[])
ax_2.set(title = 'ax_2', xticks=[], yticks=[])
ax_3.set(title = 'ax_3', xticks=[], yticks=[])
ax_4.set(title = 'ax_4', xticks=[], yticks=[])
plt.show()
