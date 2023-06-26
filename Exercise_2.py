# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

 
 
def quickSort(array, low, high):
    if low < high:
        part = partition(array, low, high)
        quickSort(array, low, part - 1)
        quickSort(array, part + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  