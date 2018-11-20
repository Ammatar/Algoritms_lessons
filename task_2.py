"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

array = [random.randint(0,50) for i in range(10)]
print(array)

def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        print(result)
    result += left[i:]
    result += right[j:]
    return result

def mergesort(array):
    if len(array) < 2:
        return array
    middle = len(array) / 2
    left = mergesort(array[:int(middle)])
    right = mergesort(array[int(middle):])
    return merge(left, right)

print(mergesort(array))
