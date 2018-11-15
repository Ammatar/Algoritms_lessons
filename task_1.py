"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.
Python 3.7.0 Windows 10 64 bit
из задания:
урок 5 задание 1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Урок 2 Задание 3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""
import sys

num = 1234567890
# вариант со строкой
# def backordr(num):
numpr = num
backord = ''

while num > 0:
    dec = num % 10
    num = num // 10
    backord = str(backord) + str(dec)

print(f'Обратный порядок для числа {numpr}: {backord}')

# вариант с умножением и остатком
num = 1234567890
numpr = num
result = 0
while num > 0:
    result = result * 10 + num % 10
    num = num // 10
print(f'Обратный порядок для числа {numpr}: {result}')

# вариант с разворотом через срез
num = 1234567890
numpr = num
result1 = str(num)[::-1]
print(f'Обратный порядок для числа {numpr}: {result1}')

print(sys.getsizeof(num), sys.getsizeof(numpr), sys.getsizeof(backord), sys.getsizeof(dec))
print('Сумма затраченной на переменные памяти',
      sys.getsizeof(num) + sys.getsizeof(numpr) + sys.getsizeof(backord) + sys.getsizeof(dec))

print(sys.getsizeof(num), sys.getsizeof(numpr), sys.getsizeof(result))
print('Сумма затраченной на переменные памяти', sys.getsizeof(num) + sys.getsizeof(numpr) + sys.getsizeof(result))

print(sys.getsizeof(num), sys.getsizeof(numpr), sys.getsizeof(backord), sys.getsizeof(dec))
print('Сумма затраченной на переменные памяти', sys.getsizeof(num) + sys.getsizeof(numpr) + sys.getsizeof(result1))
