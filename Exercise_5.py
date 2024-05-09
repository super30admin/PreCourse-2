# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

# Time Complexity : O(nlogn)
# Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# The partition function is used to divide an array using the pivot. The elements with higher value are placed to the right of the pivot and the elements with the lower value to the left
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
      if arr[j] < pivot:
          i += 1
          arr[i], arr[j] = arr[j], arr[i] # Swap the current element with the element at index i if the current element is smaller than the pivot
    
  arr[i + 1], arr[h] = arr[h], arr[i + 1]# Swap the pivot element with the next element to get the pivot at the correct position
  return i + 1 # Return pivot index


def quickSortIterative(arr, l, h):
  #write your code here
  if len(arr) == 0:
        print("Empty array")
        return
  n = len(arr)
  stack = [(0, n - 1)] # Stack that tracks the subarrays. Intialized to be the size of the original array
    
  while stack:
      l, h = stack.pop()
      if l < h: # If subarray has more than one element
          pivotIndx = partition(arr, l, h) # Find pivot position for the current subarray/array
          stack.append((l, pivotIndx - 1)) # Sort the left half
          stack.append((pivotIndx + 1, h)) # Sort the right half

# Driver code to test above 
arr = [10, 34, 99, 9, -1, -2, 7, 8, 9, 1, 5] 
n = len(arr)
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i],end = " ")
print("\n")