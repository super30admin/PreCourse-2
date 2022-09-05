# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

import random
# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low]
    i = low + 1
    for j in range(low+1, high+1):
        if arr[j] < pivot:
            (arr[j], arr[i]) = (arr[i], arr[j])
            i += 1
    (arr[low], arr[i - 1]) = (arr[i-1], arr[low])
    return i-1

def choosePivot(low, high):
    pivot = random.randint(low, high)
    return pivot

# Function to do Quick sort 
def quickSort(arr,low,high): 
  if low >= high:
    return arr
  i = choosePivot(low, high)
  (arr[low], arr[i]) = (arr[i], arr[low])
  j = partition(arr, low, high)
  quickSort(arr, low, j-1)
  quickSort(arr, j+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print(f"Sorted array is: {arr}")

  
 
