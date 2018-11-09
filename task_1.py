"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Урок 2 Задание 3
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""


# вариант со строкой
def backordr(num):
    numpr = num
    backord = ''

    while num > 0:
        dec = num % 10
        num = num // 10
        backord = str(backord) + str(dec)

    print(f'Обратный порядок для числа {numpr}: {backord}')


# backordr(1234567890)
# 1 попытка - 100 loops, best of 3: 13.7 usec per loop
# backordr(12345678901234567890)
# 2 попытка - 100 loops, best of 3: 38.4 usec per loop
# backordr(123456789012345678901234567890)
# 3 попытка - 100 loops, best of 3: 39.9 usec per loop


# вариант с умножением и остатком
def backordr_1(num):
    numpr = num
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10
    print(f'Обратный порядок для числа {numpr}: {result}')


# backordr_1(1234567890)
# 100 loops, best of 3: 8.07 usec per loop
# backordr_1(12345678901234567890)
# 100 loops, best of 3: 13.8 usec per loop
# backordr_1(123456789012345678901234567890)
# 100 loops, best of 3: 17.4 usec per loop


# вариант с разворотом через срез
def backordr_2(num):
    numpr = num
    result = str(num)[::-1]
    print(f'Обратный порядок для числа {numpr}: {result}')

# backordr_2(1234567890)
# 1100 loops, best of 3: 7.46 usec per loop
# backordr_2(1234567890)
# 100 loops, best of 3: 8.11 usec per loop
# backordr_2(1234567890)
# 100 loops, best of 3: 10 usec per loop


#
# по результатам замеров можно сделать вывод, что оптимальным решением (в том числе и с ростом значности числа) является
# срез с разворотом числа, следующим по времени выполнения математическая реализация и вариант со строкой значительно
#  проигрывает в скорости работы
