import numpy as np
import time
import csv 

def randomfunc(length):
    rand_arr = np.random.randint(-1500, 1500, length)
    return rand_arr

def HybridMergeSort(array, start, end, n):
    if len(array) <= n:
        print("Done by Insertion Sort")
        return InsertionSort(array, start, end)
    else:
        print("Done by Merge Sort")
        return MergeSort(array, start, end)

def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
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

def InsertionSort(array, start, end):
    for i in range(start + 1, end + 1):
        key_value = array[i]
        j = i - 1
        while j >= start and key_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_value
    
    return array



array = randomfunc(40000)
start_time = time.time()
arr = HybridMergeSort(array, 0, len(array) - 1, 25)
end_time = time.time()
runtime = end_time - start_time
print(arr)
print("Runtime of HybridMergeSort at",100,"is",runtime,"seconds")  

with open("HybridMergeSort.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in arr: 
        writer.writerow([i])
 
    





