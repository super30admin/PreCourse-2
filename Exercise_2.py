# Python program for implementation of Quicksort Sort 
  
# Overall complexity: 
# Bestcase: O(nlogn)
# Worst case: O(n^2)
# Average case: O(nlogn)
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    i = (low - 1)
    # last element as pivot
    pivot = arr[high]

    for j in range(low, high):
        # if the element is less than the pivot then 
        if arr[j] <= pivot:
            # increment i by 1
            i += 1
            # swap the elements at position i and j
            arr[i], arr[j] = arr[j], arr[i]
    # swap the last element in the array with element at i+1 position
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # return the index
    return (i+1)

# Function to do Quick sort
def quickSort(arr,low,high): 
    #write your code here
    # if length of array is less than or equal to 1 then
    # return array
    if len(arr) <= 1:
        return arr
    # check if end of the list is reached or not
    if low < high:
        # find the partitioning index in the list
        par_index = partition(arr, low, high)
        # sort the list before and after the partitioning index separately
        quickSort(arr, 0, par_index - 1)
        quickSort(arr, par_index + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
