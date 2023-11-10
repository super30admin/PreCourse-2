# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(low,high,arr):
    pivot, ptr = arr[high], low
    for i in range(low, high):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr 
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(low,high,arr):
    if n == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if low < high:
        pi = partition(low, high, arr)
        quickSort(low, pi-1, arr)  # Recursively sorting the left values
        quickSort(pi+1, high, arr)  # Recursively sorting the right values
    return arr
    #write your code here

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(0,n-1,arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
