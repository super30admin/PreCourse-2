# Python program for implementation of Quicksort Sort 
# Time complexity : O(n*log(n))
# Space complexity : O(n)
# give you explanation for the approach
def partition(arr,low,high):
    #Setting pivot value
    pivot, ptr = arr[high], low
    for i in range(low, high):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot value to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
            
    # Finally swappping the last element with the pointer indexed number
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr
   
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:  # Terminate recursion
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)  # Recursively sorting the left values
        quickSort(arr, pi+1, high)  # Recursively sorting the right values
    return arr
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
