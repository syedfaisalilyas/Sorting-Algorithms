import numpy as np
import time
import csv

#Problem 5
print("\n"+"Problem 5:" + "\n" + "Bubble Sort")

def BubbleSort(array_1,start,end):
    for i in range(start,end):
        flag = False
        for j in range(start,end-i):
            if array_1[j]>array_1[j+1]:
                array_1[j],array_1[j+1] = array_1[j+1],array_1[j]
                flag = True
        if(flag == False):
            return array_1
            break

def Random_A():
    array_n = np.random.randint(-1500,1500,50)
    return array_n
    
array_1 = Random_A()

start_time = time.time()
arr_b = BubbleSort(array_1,0 , len(array_1)-1)
end_time = time.time()

with open("BubbleSort.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in arr_b: 
        writer.writerow([i])

print(arr_b)

runtime = end_time - start_time
print("Runtime of Bubble Sort is",runtime,"seconds")
