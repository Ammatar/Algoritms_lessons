"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
"""
import random

array = [random.randint(-100,100) for i in range(10)]
def bubbles(array):
    n = 1
    print('исходный массив: ',array)

    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        n += 1
        #print(array, n)
    print('массив отсортированный по убыванию: ',array)

bubbles(array)