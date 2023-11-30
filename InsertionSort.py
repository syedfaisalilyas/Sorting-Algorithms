# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
import time
import csv 

def randomfunc():
    rand_arr =  np.random.randint(-1500,1500,100)
    return rand_arr
    
    
def InsertionSort(array,start,end):
    for i in range(start+1,end):
        key_value = array[i]
        j = i-1
        while j>=start and key_value<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key_value
    
    return array

array = [5,4,3,2,5]

start_time = time.time()
arr = InsertionSort(array,0,len(array)-1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of InsertionSort at",100,"is",runtime,"seconds")
print(arr)

with open("InsertionSort.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in arr: 
        writer.writerow([i])
 
        








