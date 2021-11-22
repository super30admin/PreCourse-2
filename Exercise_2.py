# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    '''
     1. Consider the first element as pivot, pivot_index = 0
     2. Compare the pivot with the next element and set low to the index greater than pivot
     3. Start the iteration for the variable high. Continue the iteration till we get small element than pivot
     4. Swap the high and low and then swap the low element with pivot
    '''
    pivot_index = low
    pivot = arr[pivot_index]
    while low < high:
        #write your code here
        #Compare the pivot with the next element. Continue the iteration till we get the element greater than Pivot
        while low < len(arr) and arr[low] <= pivot:
            low = low + 1

        #Start the iteration for the variable high. Continue the iteration till we get small element than pivot
        while arr[high] > pivot:
            high = high - 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    
    arr[pivot_index], arr[low - 1] = arr[low- 1], arr[pivot_index]
    return low

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        #write your code here
        partition_index = partition(arr,low,high)
        quickSort(arr,low,partition_index-1)
        quickSort(arr,partition_index+1,high)

# Driver code to test above 
arr = [8, 7, 10, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print (f"Sorted array is: {arr}") 
 
 
