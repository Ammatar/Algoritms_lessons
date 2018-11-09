"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
import cProfile


# Эратосфен
def primes(n):
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b


# task_2.primes(100)
# 100 loops, best of 3: 36 usec per loop
# task_2.primes(200)
# 100 loops, best of 3: 72.9 usec per loop
# task_2.primes(400)
# 100 loops, best of 3: 163 usec per loop


# Сундарам
def sundaram(n):
    b = list()
    a = [0] * n
    b.append(2)
    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0

    for i in range(1, n):
        if a[i] == 0:
            b.append(2 * i + 1)
    return b


# sundaram(50)
# 100 loops, best of 3: 18.6 usec per loop
# sundaram(100)
# 100 loops, best of 3: 38.3 usec per loop
# sundaram(200)
# 100 loops, best of 3: 83.3 usec per loop

cProfile.run('primes(4000)')
cProfile.run('sundaram(2000)')

# def test_func(n):
#     sun = sundaram(int(n/2))
#     era = primes(n)
#     print(len(sun))
#     print(len(era))
#     testprint = [i for i in era if i not in sun]
#     print(testprint)
# test_func(100000)

# алгоритм решето Сундарамы выполняется быстсрее при том, при том что n требуется вдвое меньше для одинакового результата
# оба алгоритма наращивают сложность в зависимости от объема обрабатываемых данных линейно
