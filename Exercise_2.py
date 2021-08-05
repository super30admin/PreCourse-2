# Python program for implementation of Quicksort Sort 
def partition(arr,low,high):
    # Mark the last element as the pivot
    pivot = arr[high]
    i = low
    for j in range(low,high):
        if arr[j] < pivot:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
    arr[i],arr[high] = arr[high], arr[i]
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        i = partition(arr,low,high)
        quickSort(arr, low, i-1)
        quickSort(arr, i+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
