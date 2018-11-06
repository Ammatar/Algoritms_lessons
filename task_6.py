"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

matrix = [randint(0, 100) for i in range(0, 20)]
tempmin = 100
tempmax = 0
summm = 0
print(matrix)
for i in matrix:
    if i < tempmin:
        tempmin = i

for i in matrix:
    if i > tempmax:
        tempmax = i

if matrix.index(tempmin) < matrix.index(tempmax):
    for i in range(matrix.index(tempmin) + 1, matrix.index(tempmax)):
        summm = summm + matrix[i]
else:
    for i in range(matrix.index(tempmax) + 1, matrix.index(tempmin)):
        summm = summm + matrix[i]
print(summm)
