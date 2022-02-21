from math import *
from random import *

count_positive_element = 0;
sum_element = 0;
element_equal_zero = 0;

choose_action = int(input("Выберите цифру:\n"
                          "1. Задать элементы массива самостоятельно.\n"
                          "2. Задать элементы массива рандомно, указав количество элементов в массиве.\n"
                          "Ваш выбор: "))

if choose_action == 1:
    array_list = [float(i) for i in input('Введите элементы массива: ').split()]
elif choose_action == 2:
    array_list = [uniform(-10, 10) for i in range(int(input('Введите число элементов массива ')))]
else:
    print('Ввели неверное значение, попробуйте снова!')
    exit()

for i in range(len(array_list)):
    if array_list[i] > 0:
        count_positive_element += 1

    if array_list[i] == 0:
        element_equal_zero = i

if element_equal_zero == 0:
    print('В массиве не найден элемент, равный нулю!\n')
else:
    for i in range(element_equal_zero, len(array_list)):
        sum_element += array_list[i]

if element_equal_zero != 0:
    print('Количество положительных элементов: {0:.6f} '.format(count_positive_element))
    print('Сумма элементов, расположенных после последнего элемента, равного нулю: {0:.6f}\n'.format(sum_element))

print('Массив ДО преобразования: ')
for i in range(len(array_list)):
    print('{0:.6f}'.format(array_list[i]), end=' ')
print('\n')

needIteration = True
while (needIteration):
    needIteration = False

    for i in range(1, len(array_list)):
        if abs(int(array_list[i - 1])) > 1 and abs(int(array_list[i])) <= 1:
            array_list[i - 1], array_list[i] = array_list[i], array_list[i - 1]
            needIteration = True

print('Массив ПОСЛЕ преобразования: ')
for i in range(len(array_list)):
    print('{0:.6f}'.format(array_list[i]), end=' ')
print('\n')
