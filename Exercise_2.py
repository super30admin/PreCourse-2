# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(array,start,end):
    #write your code here
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Function to do Quick sort 
def quickSort(arr,start,end):
    if start >= end:
        return
    p = partition(arr, start, end)
    quickSort(arr, start, p - 1)
    quickSort(arr, p + 1, end)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
