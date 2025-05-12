# Python program for implementation of Quicksort Sort 

# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(log n) due to recursion stack
# Did this code successfully run on Leetcode: Couldn't find this problem on Leetcode
# Any problem you faced while coding this: I need to practice more on this, it's a bit confusing

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Pointer for greater element
    i = low - 1
    
    # Compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the position from where partition is done
    return i + 1

# Function to do Quick sort 
def quickSort(arr, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)
        
        # Recursive call on the left of pivot
        quickSort(arr, low, pi - 1)
        
        # Recursive call on the right of pivot
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n): 
    print(arr[i], end=" ")
  
 
