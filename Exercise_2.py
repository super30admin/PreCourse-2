# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(nlog(n))
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
def partition(arr, low, high):

  #Define mid element based on current low and high

  mid = (low + high) / 2
  mid_element = arr[mid]

  # Iterate over array till we put the mid element at its correct place
  while low < high:

      while arr[low] <= mid_element and low < len(arr):
          low += 1

      while arr[high] > mid_element:
          high -= 1

      if low < high:
        arr[low], arr[high] = arr[high], arr[low]

  arr[high], arr[mid] = arr[mid], arr[high]

  return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    # calling quick sort function recursively while changing the low and high condition
    #  till low is less than high
    if low < high:

        pivot_element = partition(arr, low, high)

        quickSort(arr, low, pivot_element - 1)
        quickSort(arr, pivot_element + 1, high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1)
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
