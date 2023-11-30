# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:57:27 2023

@author: JUNCTION
"""

def BucketSort(array):
    B=[]
    for i in range(len(array)):
        B.append([])
    for j in array:
        number= int(j*len(array))
        B[number].append(j)
    for k in range (len(array)):
        B[k]=sorted(B[k])
    count=0
    for i in range(len(array)):
        for j in range(len(B[i])):
            array[count]=B[i][j]
            count=count+1
    return array  

# Example usage
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47,-0.1, 0.51]
sorted_array = BucketSort(arr)
print("Sorted array:", sorted_array)
