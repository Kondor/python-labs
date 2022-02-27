from math import *

x = float(input('Введите значение числа x: '))
R = float(input('Введение значение числа радиуса R: '))

y_1 = 1  # -5 <= x < -3
# y_2 = -sqrt(pow(R, 2) - pow((x + 1), 2))  # -3 <= x < -1
y_3 = -2  # -1 <= x < 2
y_4 = x - 4  # 2 <= x < 5

if (x >= -5) and (x < -3):
    y = y_1
elif (x >= -3) and (x < -1):
    R = float(input('Введение значение числа радиуса R: '))
    y_2 = -sqrt(pow(R, 2) - pow((x + 1), 2))  # -3 <= x < -1
    # чтобы не выводил -0
    if (int(y_2)) == -0:
        y = abs(y_2)
    else:
        y = y_2
elif (x >= -1) and (x < 2):
    y = y_3
elif (x >= 2) and (x < 5):
    y = y_4
else:
    y = None

if y is None:
    print('Введенное значение х не соответствует диапазону значений.\n')
    input('Нажмите Enter и повторите попытку..')
else:
    print('Значение функции числа {0:.6f} = {1:0.6f}'.format(x, y))

