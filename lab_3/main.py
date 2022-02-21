from math import *

xb = float(input('Введите начальное значение числа xbeg: '))
xe = float(input('Введите конечное значение числа xend: '))
dx = float(input('Введите значение шага числа dx: '))

xt = xb

print("+---------+---------+")
print("I    X    I    Y    I")
print("+---------+---------+")

# y_1 = 1  # -5 <= x < -3
# y_2 = -sqrt(pow(R, 2) - pow((x + 1), 2))  # -3 <= x < -1
# y_3 = -2  # -1 <= x < 2
# y_4 = x - 4  # 2 <= x < 5

while xt < xe:

    if (xt >= -5) and (xt < -3):
        y_1 = 1
        y = y_1
    elif (xt >= -3) and (xt < -1):
        y_2 = -sqrt(pow(-2, 2) - pow((xt + 1), 2))
        # чтобы не выводил -0
        if abs(int(y_2)) == 0:
            y = abs(y_2)
        else:
            y = y_2
    elif (xt >= -1) and (xt < 2):
        y_3 = -2
        y = y_3
    else:
        y_4 = xt - 4
        y = y_4

    print("I{0: 8.2f} I{1: 8.2f} I" .format(xt, y))
    xt += dx

print("+---------+---------+")

