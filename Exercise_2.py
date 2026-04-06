# // Time Complexity : Best/Average: O(nlogn), Worst O(n^2) depending on pivot. n^2 if pivot is first or last element
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this :


# // Your code here along with comments explaining your approach



# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr, low, high):
    # pivot is the item that we need to find a position for
    pivot = arr[low]
    # 'left' will track the position where elements smaller than pivot go
    left = low 

    for i in range(low + 1, high + 1): # high + 1 to include the last element
        if arr[i] < pivot:
            left += 1
            # Swap current element with the leftmost available slot
            arr[i], arr[left] = arr[left], arr[i]

    # Finally, move the pivot from the start to its correct sorted position
    arr[low], arr[left] = arr[left], arr[low]
    
    return left

# PIVOT - THE ITEM I WANT TO FIND A POSITION FOR
def quickSort(arr, low, high): 
    if low < high:
        pivotLocation = partition(arr, low, high) # returns pivot index
        # Sort elements before and after the pivot
        quickSort(arr, low, pivotLocation - 1)
        quickSort(arr, pivotLocation + 1, high)
    
# [1, 5, 8, 9, 7, 10] 
#     l        i                
# quicksort(arr,0,5)
#   pivotLocation = partition(arr,0,5)
#                       pivot = arr[0] -> 10
#                       left = 0
#                       for i = 1->5
# pivotLocation = 5
#   quickSort(arr, 0, 4)
#       partition(arr,0,4)
#   quickSort(arr, 6, 5)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
