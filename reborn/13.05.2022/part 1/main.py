import matplotlib.pyplot as plt

plt.plot((0, 3, 1, 2, 1, 5, 4, 0))
plt.show()

plt.plot((0, 0, 5, 4, 0), (0, 3, 2, 1, 0))
plt.show()

plt.scatter([0, 1, 2, 3, 4 , 5], [0, 1, 2, 3, 4 , 5])
plt.scatter([1, 2, 3, 1, 2 , 1], [2, 3, 4, 3, 4 , 4])
plt.scatter([2, 3, 4, 3, 4 , 4], [1, 2, 3, 1, 2 , 1])
plt.show()

plt.bar([6, 7, 8], [10, 15, 21])
plt.show()

plt.barh([6, 7, 8], [10, 15, 21])
plt.show()

plt.bar([5.9, 6.9, 7.9], [10, 15, 21], width = 0.2)
plt.bar([6.1, 7.1, 8.1], [6, 12, 28], width = 0.2)
plt.show()

plt.pie([5, 13, 21, 27, 10, 17])
plt.show()

plt.boxplot([[1, 5, 7, 4, 6, 10, 15],
             [-2, 5, 7, 4, 6, 10, 15],
             [-4, 5, 7, 4, 6, 10]])
plt.show()
