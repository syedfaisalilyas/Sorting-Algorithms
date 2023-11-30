
#Problem 6
#Selection Sort

import numpy as np
import time
import csv

print("\n" + "Problem 6:" + "\n" "Selection Sort ")

def Random_A():
    array_n = np.random.randint(-1500,1500,50)
    return array_n



def SelectionSort(array,start,end):
    for i in range(start,end):
        min_index = i
        min_num = array[i]
        
        for j in range(i,end+1):
            if array[j] < min_num:
                min_num = array[j]
                min_index = j
                
        temp = array[i]
        array[i] = min_num
        array[min_index] = temp
    
    return array

    

array_n = Random_A()

start_time = time.time()
arr_a = SelectionSort(array_n, 0, len(array_n)-1)
end_time = time.time()


with open("SelectionSort.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in arr_a: 
        writer.writerow([i])

print(arr_a)

runtime = end_time - start_time
print("Runtime of Selection Sort is",runtime,"seconds")
    