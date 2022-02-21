from math import (pow, sqrt)

m = float(input('Введите значение m: '))

tmp_numerator = pow((3*m + 2), 2) - 24*m
tmp_denominator = 3*sqrt(m) - 2/sqrt(m)

z_1 = sqrt(tmp_numerator)/tmp_denominator
z_2 = sqrt(m)

print('Значение z1 = {0:.6f}'.format(z_1))
print('Значение z2 = {0:.6f}'.format(z_2))
