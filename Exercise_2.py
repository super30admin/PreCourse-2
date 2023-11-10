# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1 # Initialize index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 # returning the pivot index

def quickSort(arr,low,high):
    if low < high:
        pivot = partition(arr, low, high)
        # Recursively sorting partitions
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print(f"Sorted array is:{arr}")