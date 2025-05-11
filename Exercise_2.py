# Time Complexity : O(n log n) on average, O(n^2) in the worst case
# Space Complexity : O(log n) on average for the call stack, O(n) in the worst case
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No issues

# I use the last element as pivot, move smaller items before it, then place pivot in its right spot.
def partition(arr,low,high):

    # pick pivot as the last element
    pivot = arr[high]
    # i will mark the boundary of items <= pivot
    i = low - 1

    # go through each item from low to high-1
    for j in range(low, high):
        # if current item is <= pivot, expand the boundary and swap it in
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # put pivot right after the last smaller item
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # return the pivot’s final index
    return i + 1  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    # only sort when there are at least two items
    if low < high:
        # partition returns pivot index
        pi = partition(arr, low, high)
        # sort everything before pivot
        quickSort(arr, low, pi - 1)
        # sort everything after pivot
        quickSort(arr, pi + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
