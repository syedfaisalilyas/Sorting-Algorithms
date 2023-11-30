# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:30:43 2023

@author: JUNCTION
"""
def CountingSort(array):
    min_num = min(array)
    max_num = max(array)
    k = max_num - min_num + 1

    # Adjust the array to make all numbers non-negative
    for i in range(len(array)):
        array[i] += abs(min_num)

    # Initialize count and output arrays
    count = [0] * k
    output = [0] * len(array)

    # Count the occurrences of each element in the adjusted array
    for num in array:
        count[num] += 1

    # Modify the count array to store the cumulative count of elements
    for i in range(1, k):
        count[i] += count[i - 1]

    # Build the output array based on the sorted order
    for num in reversed(array):
        j = num
        output[count[j] - 1] = num
        count[j] -= 1

    # Adjust the output array back to the original values
    for i in range(len(output)):
        output[i] -= abs(min_num)

    return output

array = [-5, -10, 0, -3, 8, 5, -1, 10]
sortedArray = CountingSort(array)
print(sortedArray)
