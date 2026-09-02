# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
There are a lot of partitions that I could possibly use. The most efficient partition I understand easily is the Lomuto partition.

I recognize that Hoare's partition is the fastest of all, but I have stuck with what I understand for now

Basically as I understand it we keep track of the smaller element relative to the pivot and keep moving them left. Once we're done we swap the pivot into it's appropriate position,
and all elements less than it will be to the left and all elements to the right will be greater. We then keep doing this recursively until we've processed the entire array
'''
def partition(arr, low, high):
    pivot = arr[high]
    smallerIndex = low - 1

    for index in range(low, high):
        # Move all smaller elements to the left side
        if arr[index] < pivot:
            smallerIndex += 1
            arr[smallerIndex], arr[index] = arr[index], arr[smallerIndex]

    arr[smallerIndex + 1], arr[high] = arr[high], arr[smallerIndex + 1]
  
    return smallerIndex + 1
  

# Function to do Quick sort 
def quickSort(arr, low, high): 
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
