"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

matrix = [randint(-100, 100) for i in range(0, 20)]
matrix_under_zero = []
temp_max = -100
print(matrix)
for i in matrix:
    if i < 0:
        matrix_under_zero.append(i)

for i in matrix_under_zero:
    if i > temp_max:
        temp_max = i
print('Максимальное отрицательное число ряда: ', temp_max)
