from random import *

x = int(input('Введите челое число(нижнюю границу диапозона): '))
y = int(input('Введите челое число(верхнюю границу диапозона): '))
d = randint(x, y)
print ('Случайное число в указаном диапозоне: ', d)

x = float(input('Введите целое или дробное число(нижнюю границу диапозона): '))
y = float(input('Введите целое или дробное число(верхнюю границу диапозона): '))
s = uniform(x, y)
print('Случайное число в указаном диапозоне: ',s)

x = str(input('Введите букву(нижнюю границу диапозона): '))
y = str(input('Введите букву(верхнюю границу диапозона): '))
abc = 'abcdefghijklmnopqrstuvwxyz'
abc = list(abc)
lett = choice(abc[abc.index(x):abc.index(y)])
print ('Случайная буква в указаном диапозоне: ', lett)
