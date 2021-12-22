# Python program for implementation of Quicksort  

# Time Complexity : O(n log n), O(n^2) worst case
# Space Complexity : O(log n)
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No
  
# In this function, we choose a pivot and partition the array
# In the end of this function, the elements smaller than pivot will be on left of pivot
# All elements greater will be on the right of pivot
def partition(arr,low,high):            

    # choosing first element as pivot
    pivot_value = arr[low]

    # Since first element is pivot, array will start at the next element and end at last element index
    left = low + 1
    right = high

    finished = False
    while not finished:

        # As long as there are elements in arr and
        # And value of first element next to pivot is smaller than pivot
        # No need to do anything as smaller element is on the left. So just to increment to the next position
        while left <= right and arr[left] <= pivot_value:       
            left = left + 1

        # Same as above, as long as elements greater than pivot are on the right just go the the previous index to compare
        while right >= left and arr[right] >= pivot_value:
            right = right - 1

        # When no more elements to compare, exit loop
        if right < left:
            finished = True

        # First smaller element on right or higher element on the lelft we encouter, 
        # swap values with corresponding right/lelft elements
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    # When split point is reached, swap pivot value with the right index value
    temp = arr[low]
    arr[low] = arr[right]
    arr[right] = temp

    return right
  

# Function to do Quick sort 
def quickSort(arr,low,high):

    if(low < high):

        splitpoint = partition(arr, low, high)

        quickSort(arr, low, splitpoint - 1)
        quickSort(arr, splitpoint + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
