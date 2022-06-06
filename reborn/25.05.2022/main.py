import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.animation as animation

x = np.linspace(-3, 3, 200)
y = x*(x + 2)*(x - 2)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
fig.savefig('charts/мой график')

#  Создаем многостраничный pdf файл:
pdf_file = PdfPages('charts/Laplace.pdf')
#  Параметры распределения Лапласа:
loc = np.linspace(1, 2, 5)
scale = np.linspace(5, 10, 5)
for l in loc:
    fig, axes = plt.subplots(5, 1)
    for s in scale:
        laplace = np.random.laplace(l, s, size=1000)
        i = list(scale).index(s)
        axes[i].violinplot(laplace, vert = False)
        axes[i].set_title('scale = ' + str(s))
    fig.suptitle('loc = ' + str(l), y = 0.92, x = 0.51, fontsize = 15)
    fig.set_figheight(10)
    #  Увеличим расстояние между Axes:
    fig.subplots_adjust(hspace=0.5)
    #  Сохраняем область "Figure" на отдельной странице:
    pdf_file.savefig(fig)
#  Сохраняем и закрываем документ:
pdf_file.close()

t = np.linspace(-4, 4, 300)
fig, ax = plt.subplots()
#  Создаем функцию, генерирующую картинки
#  для последующей "склейки":
def animate(i):
    ax.clear()
    line = ax.plot(t, np.sin(i*t))
    return line
#  Создаем объект анимации:
sin_animation = animation.FuncAnimation(fig,
                                      animate,
                                      frames=np.linspace(2, 4, 30),
                                      interval = 10,
                                      repeat = False)
#  Сохраняем анимацию в виде gif файла:
sin_animation.save('charts/моя анимация.gif',
                 writer='imagemagick',
                 fps=30)


