# Просим пользователя ввести год
x = int(input('Введите год'))
# Вычисляем високосность
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    # выводим решение если год високосный
    print('Год високосный')
else:
    # выводим решение если год не високосный
    print('Год не високосный')

#
