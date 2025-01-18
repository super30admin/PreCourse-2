# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
import random
def partition(arr,low,high):
  
  
    #write your code here
    # Select a random pivot and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Now use the last element as the pivot
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        # Partition the array and get the pivot index
        pivot = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
