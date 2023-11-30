

import numpy as np
import time
import csv 

def randomfunc(length):
    rand_arr = np.random.randint(-1500, 1500, length)
    return rand_arr

def MergeSort(array, start, end):
    if start<end:
        mid = int((start + end) / 2)
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        return Mergefunc(array, start, mid, end)
    else:
        return array

def Mergefunc(array, start, mid, end):
    left_array = array[start:mid + 1]
    right_array = array[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            k += 1
            i += 1
        else:
            array[k] = right_array[j]
            k += 1
            j += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return array


array = randomfunc(100)
start_time = time.time()
sorted_array = MergeSort(array, 0, len(array) - 1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of InsertionSort at",100,"is",runtime,"seconds")  
print(sorted_array)


with open("MergeSort.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in sorted_array: 
        writer.writerow([i])
 
    
    
  