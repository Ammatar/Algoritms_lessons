n = int(input('введите натуральное число'))
num1 = 0
num2 = 0

for i in range(1, n+1):
    num1 += i
num2 = n * (n + 1) // 2

if num1 == num2:
    print('True')
else:
    print('False')