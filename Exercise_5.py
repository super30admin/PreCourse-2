# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
"""
Time - O(n^2)
Space - O(n)
Idea - We divide the list according to partition and then sort the left and right list of the partition
"""
def quickSortIterative(arr, l, h):
  if len(arr) < 1:
    return None
  divide(arr, l, h)


def divide(arr, lo, hi):  
    stack = []
    stack.append((lo, hi))

    while stack:
      start, end = stack.pop(0)
    
      pivot = partition(arr, start, end)

      if pivot-1 > start:
        stack.append((start, pivot-1))

      if pivot+1 < end:
        stack.append((pivot+1, end))

def partition(arr,low,high):
    pivot = arr[low]
    swap_index = low + 1

    for i in range(low+1, high+1):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    
    arr[low], arr[swap_index-1] = arr[swap_index-1], arr[low]
    return swap_index-1

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i])




