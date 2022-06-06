import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.linspace(0, 5, 100)
y = x*(x - 2)*(x - 4)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
#  Добавляем подписи к осям:
ax.set_xlabel('время (с)')
ax.set_ylabel('скорость (м/с)')
plt.show()

x = np.linspace(-10, 10, 200)
y = 0.01 * (x + 9) * (x + 6) * (x - 6) * (x - 9) * x
fig, ax = plt.subplots()
ax.plot(x, y, color='r', linewidth=3)
#  Устанавливаем интервал основных и
#  вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
#  Настраиваем вид основных тиков:
ax.tick_params(axis='both',  # Применяем параметры к обеим осям
               which='major',  # Применяем параметры к основным делениям
               direction='inout',  # Рисуем деления внутри и снаружи графика
               length=20,  # Длинна делений
               width=4,  # Ширина делений
               color='m',  # Цвет делений
               pad=10,  # Расстояние между черточкой и ее подписью
               labelsize=15,  # Размер подписи
               labelcolor='r',  # Цвет подписи
               bottom=True,  # Рисуем метки снизу
               top=True,  # сверху
               left=True,  # слева
               right=True,  # и справа
               labelbottom=True,  # Рисуем подписи снизу
               labeltop=True,  # сверху
               labelleft=True,  # слева
               labelright=True,  # и справа
               labelrotation=45)  # Поворот подписей
#  Настраиваем вид вспомогательных тиков:
ax.tick_params(axis='both',  # Применяем параметры к обеим осям
               which='minor',  # Применяем параметры к вспомогательным делениям
               direction='out',  # Рисуем деления внутри и снаружи графика
               length=10,  # Длинна делений
               width=2,  # Ширина делений
               color='m',  # Цвет делений
               pad=10,  # Расстояние между черточкой и ее подписью
               labelsize=15,  # Размер подписи
               labelcolor='r',  # Цвет подписи
               bottom=True,  # Рисуем метки снизу
               top=True,  # сверху
               left=True,  # слева
               right=True)  # и справа
#  Добавляем линии основной сетки:
ax.grid(which='major',
        color='m')
#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#  Теперь можем отдельно задавать внешний вид вспомогательной сетки:
ax.grid(which='minor',
        color='m',
        linestyle=':')
fig.set_figwidth(12)
fig.set_figheight(8)
plt.show()

labels = ['Контрольная\nгруппа № %i' % i for i in range(1, 6)]
value = (12, 24, 18, 11, 6)
position = np.arange(5)
fig, ax = plt.subplots()
ax.barh(position, value)
#  Устанавливаем позиции тиков:
ax.set_yticks(position)
#  Устанавливаем подписи тиков
labels = ax.set_yticklabels(labels,
                   fontsize = 15,    #  Размер шрифта
                   color = 'b',    #  Цвет текста
                   rotation = 45,    #  Поворот текста
                   verticalalignment =  'center')    #  Вертикальное выравнивание

fig.set_figwidth(10)
fig.set_figheight(8)
plt.show()
