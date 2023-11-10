# Time Complexity - O(nlog(n))
# Space Complexity - O(nlog(n))

# Python program for implementation of Quicksort Sort   

# give you explanation for the approach
def partition(arr,low,high):  
  
    #write your code here
    # Here, last element of the array has been taken as a pivot element. 
    # And first element of the array as a pointer.
    i = low
    j = high - 1
    pivot = arr[high]
    while i < j:
        while i < high and arr[i] < pivot:
            i += 1
            
        while j > low and arr[j] >= pivot:
            j -= 1
        # swapping the elements greater than the pivot to the front.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    # At last, swapping the last element with the pointer positioned number.
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
        
    return i

# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    # return array if it contain only one element.
    if len(arr) == 1:
        return arr
    
    # else assume one pivot element and do partition around it.
    if low < high:
        partition_position = partition(arr, low, high)
        
        # recursively sorting the elements present on the left of the pivot element.
        quickSort(arr, low, partition_position - 1) 
        
        # recursively sorting the elements present on the right of the pivot element.
        quickSort(arr, partition_position + 1, high) 
    
    return arr



# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
