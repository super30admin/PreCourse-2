# Time Complexity : O (nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort 
from sympy import O


def mergeSort(arr):
  # We will split the array until we reach the last individual elements of the array.
  # We will do this recursively.
  if len(arr)>1:
    mid = len(arr)//2
    arr_left = arr[:mid]
    arr_right = arr[mid:]
    mergeSort(arr_left)
    mergeSort(arr_right)
    # Pointers for left subarray, right subarray and main array respectively.
    l = 0
    r = 0
    m = 0

    # Now we will merge the sorted subarrays into one.
    while l < len(arr_left) and r < len(arr_right):
      if arr_left[l] < arr_right[r]:
        arr[m] = arr_left[l]
        l = l+1
      else:
        arr[m] = arr_right[r]
        r = r+1
      m = m+1
    
    # If there are any elements remaining, we will add them at the end.
    while l < len(arr_left):
      arr[m] = arr_left[l]
      l += 1
      m += 1
    
    while r < len(arr_right):
      arr[m] = arr_right[r]
      r += 1
      m += 1
    



  
  
  
# Code to print the list 
def printList(arr): 
    
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [123, 34, 56, 2, 3, 890, 45,]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
