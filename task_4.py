"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
count = int(input('введите целое число (количество элементов ряда): '))
countpr = count
num = 1
numsum = 0
while count > 0:
    numsum = numsum + num
    num = -( num / 2)

    count -= 1
print(f'сумма рядя для {countpr} элементов {numsum}')