# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes on Geeksforgeeks
# Any problem you faced while coding this : No

# give you explanation for the approach

# in the parition function, finding the partition position of the pivot element
def partition(arr,low,high):
    #write your code here
    # taking first element as pivot means find the sorted position of this pivot element
    pivot_index = low
    pivot_element = arr[pivot_index]

    # start with the next element of the pivot to start comparing
    i = pivot_index + 1 
    j = high

    # find the position of pivot. until the low and high intersect, keep going
    while i <= j:
        
        # find the next element larger than pivot so i = pivot_index + 1 
        # keep incrementing low until we find an element that is larger than pivot
        while i <= j and arr[i] <= pivot_element:
            i += 1
        # find the next element smaller than pivot
        # keep decrementing high until we find an element that is smaller than pivot
        while i <= j and arr[j] >= pivot_element:
            j -= 1
        if i <= j:
            # swapping these elements
            arr[i], arr[j] = arr[j], arr[i]

    # place the pivot element on its sorted position(j is the sorted position because any element after j is greater 
    # and any element before j is smaller) and that positional element on the very first
    arr[pivot_index], arr[j]  =  arr[j], arr[pivot_index]

    # returning the sorted element position which is our partition
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        # taken the sorted element position in the variable
        partition_index = partition(arr,low,high)
        # perform quicksort on LHS
        quickSort(arr, low, partition_index)
        #perform quicksort on RHS
        quickSort(arr, partition_index+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("i",arr[i])
  
 
