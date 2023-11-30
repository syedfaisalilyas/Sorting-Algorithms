# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 07:55:25 2023

@author: JUNCTION
"""

def QuickSort(Array, start, end):
    if start < end:
        pivot_index = partition(Array, start, end)
        
        QuickSort(Array, start, pivot_index - 1)
        QuickSort(Array, pivot_index + 1, end)

def partition(Array, start, end):
    pivot = Array[end]
    i = start - 1
    for j in range(start, end):
        if Array[j] <= pivot:
            i = i + 1
            Array[i], Array[j] = Array[j], Array[i]
    Array[i + 1], Array[end] = Array[end], Array[i + 1]
    
    return i + 1

Array = [9, 8, 8, 7, 7, 6, 5, 4, 3, 4, 2, 1]
QuickSort(Array, 0, len(Array) - 1)
print(Array)
