# Python program for implementation of Quicksort Sort 
import random
# give you explanation for the approach

# Using Lomuto's Partitioning - O(n), in-place partitioning algorithm - Comments in-line

def partition(arr,start,end):
    # Pick a random pivot index, randomization might optimize the algorithm
    # How? If we pick a fixed pivot - start/end/mid, and if the array has a bunch of duplicates
    # randomization reduces the probability of duplicates being repeatedly picked as pivots for partitioning. 
    random_pivot_index = random.randint(start, end)
    
    # Swap the pivot index with the start index of the array, now the start is the pivot
    arr[random_pivot_index], arr[start] = arr[start], arr[random_pivot_index]
    pivot = arr[start]
    
    # Visualize two zones in the partitioned array
    # Orange zone - elements less than the pivot
    # Green zone - elements greater than pivot
    # Goal is to swap elements till we have all elements < pivot in the left half and 
    # elements > pivot in the right half
    orange = start
    # traverse the array with green pointer
    for green in range(start + 1, end + 1):
        # if an element is less than pivot(orange), increment orange pointer and swap
        if arr[green] <= pivot:
            orange += 1
            arr[orange], arr[green] = arr[green], arr[orange]
    
    # Move start back to it's original position
    arr[start], arr[orange] = arr[orange], arr[start]
    
    # Return the pivot index of the partitioned array
    return orange

# Function to do Quick sort 
def quickSort(arr,low,high): 
    helper(arr, low, high)

def helper(arr, start, end):
    # Base case
    if start >= end:
        return
    p = partition(arr, start, end)
    # Recursively partition left and right subarrays
    helper(arr, start, p - 1)
    helper(arr, p + 1, end)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
# Running Time analysis
# It depends on the sizes of the two partitions
# Best-case = Partition splits the numbers evenly, and we get a similar recursion as mergesort -> O(n * log n) 
# Worst-case = One partition empty, the other has all the elements. We get a similar recursion as insertion sort -> O(n**2) 
# Average-case -> O(n * log n)
 
