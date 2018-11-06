"""
4. Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

x = 20
matrix = [randint(0, 100) for i in range(1, x)]
print(matrix)

number = matrix[0]
maxbuffer = 1
for i in range(x - 1):
    buffer = 0
    for m in range(1, x - 1):
        if matrix[i] == matrix[m]:
            buffer += 1
    if buffer > maxbuffer:
        maxbuffer = buffer
        number = matrix[i]
if maxbuffer > 1:
    print(maxbuffer, 'раз встречается', number)
else:
    print('нет повторяющихся элементов')
# print(buffer)
