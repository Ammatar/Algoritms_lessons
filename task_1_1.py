"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
Python 3.7.0 Windows 10 64 bit
из задания:
Урок 3 задание 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint
import sys

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

print(sys.getsizeof(matrix), sys.getsizeof(matrix_under_zero), sys.getsizeof(temp_max), sys.getsizeof(i))
print('Сумма затраченной на переменные памяти',
      sys.getsizeof(matrix) + sys.getsizeof(matrix_under_zero) + sys.getsizeof(temp_max) + sys.getsizeof(i))
