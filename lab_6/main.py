from math import *
import turtle as turtle


# Функция кривых
def fun_graph(x):
    if (x >= -6) and (x < -5):
        y = None
    elif (x >= -5) and (x < -3):
        y_1 = 1
        y = y_1
    elif (x >= -3) and (x < -1):
        y_2 = -sqrt(pow(-2, 2) - pow((x + 1), 2))
        # if (x >= -2.990001) and (x <= -2.98):
        if (x >= -2.990001) and (x <= -2.976):
            y = None
        else:
            y = y_2
    elif (x >= -1) and (x < 2):
        y_3 = -2
        y = y_3
    elif x <= 5:
        y_4 = x - 4
        y = y_4
    else:
        y = None
    return y


# Функция рисования оси
def draw_axes(txy, axy='X'):
    turtle.penup()
    if axy == 'X':
        turtle.goto(txy[0], 0)
        turtle.pendown()
        turtle.goto(txy[1], 0)
    else:
        turtle.goto(0, txy[0])
        turtle.pendown()
        turtle.goto(0, txy[1])


# Функция нанесения делений и надписей
def draw_mark(txy, axy='X'):
    turtle.penup()

    for i in range(txy[0], txy[1]):
        if axy == 'X':
            turtle.goto(i, 0)
            turtle.pendown()
            turtle.goto(i, 0.2)
            turtle.penup()
            turtle.goto(i, -0.5)
            turtle.write(str(i))
        else:
            turtle.goto(0, i)
            turtle.pendown()
            turtle.goto(0.2, i)
            turtle.penup()
            turtle.goto(0.2, i)
            turtle.write(str(i))


# Функция рисования стрелки
def draw_arrow(txy, ax='X'):
    # Параметры многоугольника
    a = [0.1, 0, -0.1]
    b = [-0.1, 0.3, -0.1]

    turtle.up()
    turtle.goto(0, 0)  # в начало
    turtle.begin_poly()  # начинаем запись вершин

    for i in range(2):  # для всех вершин
        turtle.goto(a[i], b[i])  # многоугольника

    turtle.end_poly()  # останавливаем запись
    p = turtle.get_poly()  # ссылка на многоугольник

    # регистрируем новую форму черепашке
    turtle.register_shape("myArrow", p)
    turtle.resizemode("myArrow")
    turtle.shapesize(1, 2, 1)  # растягиваем (пример)

    if ax == 'X':  # для оси X
        turtle.tiltangle(0)  # угол для формы
        turtle.goto(txy[1] + 0.2, 0)  # к месту стрелки
        pw = [int(txy[1]), -1.0]  # надпись
    else:  # для оси Y
        turtle.tiltangle(90)  # угол для формы
        turtle.goto(0, txy[1] + 0.2)  # к месту стрелки
        pw = [0.2, int(txy[1])]  # надпись

    turtle.stamp()  # оставить штамп - стрелка

    # надпишем ось
    turtle.goto(pw)  # к месту надписи
    turtle.write(ax, font=("Arial", 14, "bold"))


# Размеры по горизонтали и вертикали
aX = [-6, 6]
aY = [-3, 2]

# Размер главного окна
Dx = 800
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
turtle.setup(Dx, Dy)
turtle.reset()

# Число точек рисования для меньшей погрешности
nMax = 1000

# Создание системы координат
turtle.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

# Увеличение главного окна
turtle.setup(Dx + 500, Dy + 500)

# Ось - ox, метки, стрелка
draw_axes(aX, 'X')
draw_mark(aX, 'X')
draw_arrow(aX, 'X')

# Ось - oy, метки, стрелка
draw_axes(aY, 'Y')
draw_mark(aY, 'Y')
draw_arrow(aY, 'Y')

# Параметры
turtle.color("green")  # цвет линии
turtle.width(3)  # толщина
dx = (aX[1]-aX[0])/nMax  # шаг

# Начало координат
x = aX[0]
y = fun_graph(x)
if y is None:
    turtle.up()
    turtle.goto(x, 0)
else:
    turtle.goto(x, y)
    turtle.down()

# Рисование кривых
while x <= aX[1]:

    y = fun_graph(x)
    if y is None:
        turtle.up()
        turtle.goto(x, 0)
    elif (x >= -2.9640001) and (x <= -2.964):
        turtle.up()
        turtle.goto(x, 0)
        turtle.down()
    else:
        turtle.goto(x, y)
        turtle.down()
    x = x + dx

turtle.done()
