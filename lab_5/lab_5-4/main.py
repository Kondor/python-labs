from math import *
from random import *

count_positive_element = 0
sum_element = 0
element_equal_zero = 0

with open('file_input.txt', 'r') as inf:
    array_list = [float(i) for i in inf.read().split(',')]

for i in range(len(array_list)):
    if array_list[i] > 0:
        count_positive_element += 1

    if array_list[i] == 0:
        element_equal_zero = i

with open('file_output.txt', 'w') as ouf:

    if element_equal_zero == 0:
        ouf.write('В массиве не найден элемент, равный нулю!\n')
    else:
        for i in range(element_equal_zero, len(array_list)):
            sum_element += array_list[i]

    if element_equal_zero != 0:
        ouf.write('Количество положительных элементов: {0:d} \n'.format(count_positive_element))
        ouf.write('Сумма элементов, расположенных после последнего элемента, равного нулю: {0:.6f}\n\n'
                  .format(sum_element))

    ouf.write('Массив ДО преобразования: \n')
    for i in range(len(array_list)):
        ouf.write('{0:.6f} '.format(array_list[i]))
    ouf.write('\n\n')

    needIteration = True
    while needIteration:
        needIteration = False

        for i in range(1, len(array_list)):
            if (abs(int(array_list[i - 1])) > 1) and (abs(int(array_list[i])) <= 1):
                array_list[i - 1], array_list[i] = array_list[i], array_list[i - 1]
                needIteration = True

    ouf.write('Массив ПОСЛЕ преобразования: \n')
    for i in range(len(array_list)):
        ouf.write('{0:.6f} '.format(array_list[i]))
    ouf.write('\n')
