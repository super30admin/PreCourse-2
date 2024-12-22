# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1
  
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        x = partition(arr, low, high)
        quickSort(arr, low, x - 1)
        quickSort(arr, x + 1, high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
