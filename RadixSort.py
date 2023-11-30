# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:08:59 2023

@author: JUNCTION
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:30:43 2023

@author: JUNCTION
"""

def counting_sort(array, exp):

    min_num = min(array)
    max_num = max(array)
    k = max_num - min_num + 1

    # Adjust the array to make all numbers non-negative
    for i in range(len(array)):
        array[i] += abs(min_num)

    output = [0] * len(array)
    count = [0] * k  # Counting array for negative and positive digits (-9 to 10)

    for num in array:
        index = (num // exp) % 10
        count[index] += 1  # Adjust index to fit within the counting array

    for i in range(1,k):
        count[i] += count[i - 1]

    for num in reversed(array):
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    for i in range(len(output)):
        output[i] -= abs(min_num)

    return output

def radix_sort(array):
    max_num = max(array)
    exp = 1
    while max_num / exp > 0:
        array = counting_sort(array, exp)
        exp *= 10

    return array

array = [-5, -10, 0, -3, 8, 5, -1, 10,-99]
sortedArray = radix_sort(array)
print(sortedArray)


