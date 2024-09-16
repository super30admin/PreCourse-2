# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    ind = low
    pivot = arr[ind]
    while low < high:
        while low<len(arr) and arr[low]<=pivot:
            low+=1
        while high>=0 and arr[high]>pivot:
            high-=1
        if low < high:
            arr[low],arr[high]=arr[high],arr[low] 
    arr[high], arr[ind] = arr[ind], arr[high]
    return high

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
