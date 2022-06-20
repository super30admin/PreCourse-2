# Python program for implementation of Quicksort Sort 
  
# TC Best, Avg = o(nlogn) || Worst = o(n*n)
# SC Best, Avg = o(logn) || Worst = o(n)
    
# give you explanation for the approach
    # This code is a recursive divide and conquer method.
    # first we chose a pivot element, it can be random, here the pvt is chosen as a last element of the partiiton.  
    # Swap the element less than pivot in left subarray, swaping the element greater than pivot in right subarray.
    # Then quicksorts the left and right subarray recursively.    
def partition(arr,low,high):
    l = low
    h = high -1
    pvt = arr[high]
    while l < h:
        while l < high and arr[l] < pvt:
            l += 1
        while h > low and arr[h] >= pvt:
            h -= 1
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]
    if arr[l] > pvt:
        arr[l], arr[high] = arr[high], arr[l]
    return l                 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high:
        return
    partition_ = partition(arr,low,high)   
    quickSort(arr,low,partition_ - 1)
    quickSort(arr,partition_ + 1, high)

    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
