# Python program for implementation of Quicksort Sort 

# Time Complexity : ON(logn) - as the steps taken to reach the answer is logn, as at every step, the n is reduced by half.
# Space Complexity : O(N) - Recursion stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes, I was doing swap function in python with swap(a, b). As the variables are passed by value and not
# by reference in Python, the array elements were not getting updated. Hence, changed the method and passed the array and indices for the swap to work.

# Quick sort is called with arr, low, high, then we first identify the partition_index 
# 4 2 1 5 3 6
# 0 1 2 3 4 5
# pivot = 4,
# We iterate i= 0 to i=3 until we find the element that is greater than pivot as it needs to be swapped
# We iterate j = 5 to j = 4 until we find the element that is less than pivot as it needs to be swapped
# swap arr[3] and arr[4] so that low values are on to the left side and high values are on to right. 
# 4 2 1 3 5 6
# Now i is at 3, and j is at 4, so we iterate further in the while loop, we increment i to be 4 and j to be 3, however as i is not less
# than j, we do not do the swap, and break the loop. Hence now, we
# Now swap the pivot element to its original location which is supposed to be j, swapping arr[j] with pivot and then return the 
# partition_index which is j as it is the original location. 
# 3 2 1 4 5 6 
# Now, the elements less than the pivot are to the left and elements greater than pivot are to the right.
# repeat the recursive call by dividing the array from (low, partition_index-1) and (partition_index+1, high)

def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low]
    i, j = low, high
    while i<j:
        while arr[i] <= pivot and i<high:
            i += 1
        while arr[j] > pivot and j>low:
            j -= 1
        if i<j:
            swap(arr, i, j)

    swap(arr, j, low)
    return j

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)

# write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
