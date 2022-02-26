from math import (pow, sqrt)

# m = float(input('Введите значение m: '))

with open('file_input.txt', 'r') as inf:
    m = inf.readline()
    m = m.strip('Input m: ')
    m = float(m)
    print(m)

tmp_numerator = pow((3*m + 2), 2) - 24*m
tmp_denominator = 3*sqrt(m) - 2/sqrt(m)

z_1 = sqrt(tmp_numerator)/tmp_denominator
z_2 = sqrt(m)

print('Значение z1 = {0:.6f}'.format(z_1))
print('Значение z2 = {0:.6f}'.format(z_2))

with open('file_output.txt', 'w') as ouf:
    # Вывести шапку таблицы в файл
    ouf.write('+===========+============+============+\n')
    ouf.write('I    m      I    Z_1     I     Z_2    I\n')
    ouf.write('+===========+============+============+\n')
    ouf.write('I{0:10.2f} I{1: 10.6f}  I{2: 10.6f}  I\n'.format(m, z_1, z_2))
    ouf.write('+===========+============+============+\n')
