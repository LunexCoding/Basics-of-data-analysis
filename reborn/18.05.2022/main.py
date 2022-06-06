import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 10000)
fig, ax = plt.subplots()
ax.hist(data, bins = 50, rwidth = 0.4)
ax.set_title('Нормальное распределение')
plt.show()

mu, sigma = 1.1, 2.9
data = np.random.normal(mu, sigma, 10000)
fig, ax = plt.subplots()
ax.hist(data, bins = 50, rwidth = 0.4)
ax.set_title(r'$p(x)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$')
plt.show()

x = np.linspace(-3*np.pi, 3*np.pi, 200)
y1 = np.sin(x) - 2
y2 = np.cos(x) + 2
y3 = np.sinc(x)
fig, ax = plt.subplots()
ax.plot(x, y1, label = 'sin(x)')
ax.plot(x, y2, label = 'cos(x)')
ax.plot(x, y3, label = r'$\frac{sin(x)}{x}$')
ax.legend()
fig.set_figheight(5)
fig.set_figwidth(8)
plt.show()

x = np.linspace(-3*np.pi, 3*np.pi, 200)
y = np.sinc(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
plt.show()

x = np.linspace(-5, 5, 100)
y = (x - 2)*(x + 2)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
#  Вертикальные линии:
ax.vlines(0, y.min(), y.max())
ax.vlines(-2, y.min(), y.max(), color = 'r')
ax.vlines(2, y.min(), y.max(), color = 'r')
#  Горизонтальные динии:
ax.hlines(0, -5, 5)
ax.hlines(-4, -5, 5)
plt.show()
