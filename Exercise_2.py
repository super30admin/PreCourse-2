# Time Complexity : O(nlog(n))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(array,low,high):
  
  # rightmost element as pivot
    pivot = array[high]
  
  # Pointer for greater element
    i = low - 1
  
    for j in range(low, high):
        if array[j] <= pivot:
        # If element smaller than pivot is found
        # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
  
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    # Return the position from where partition is done
    return i + 1
  

# Function to do Quick sort 
def quick_sort(array,low,high): 
    
    if low < high:
  
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
  
        # Recursive call on left side
        quick_sort(array, low, pi - 1)

        # Recursive call on right side
        quick_sort(array, pi + 1, high)

#Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quick_sort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
