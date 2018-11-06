"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint

matrix = []
tempmin = 100
tempmax = 0

for _ in range(1, 15):
    matrix.append(randint(0, 100))

print(matrix)
for i in matrix:
    if i < tempmin:
        tempmin = i
    else:
        pass
print(tempmin, matrix.index(tempmin))

for i in matrix:
    if i > tempmax:
        tempmax = i
    else:
        pass
print(tempmax, matrix.index(tempmax))

matrix[matrix.index(tempmin)] = tempmax
matrix[matrix.index(tempmax)] = tempmin

print(matrix)
