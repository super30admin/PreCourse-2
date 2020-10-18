# Python program for implementation of MergeSort 

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def mergeSort(arr):
  """
  Divide into 2 halves recursively
  Merge broken pieces in sorted order
  """
  l, r = 0, len(arr)-1
  helper(arr, l, r)


def helper(arr, l, r):
  """
  Helper function to break to smallest elements recursively
  """
  # Base condition is right pointer should be greater than left pointer
  if r > l:
      # Calculate the middle pointer
      m = l + (r-l)//2
      # Call helper recursively by breaking the list
      helper(arr, l, m)
      helper(arr, m+1, r)
      # Merge the list
      merge(arr, l, m, r)

def merge(arr, l, m, r):  
  """
  Merge function creates two lists left and right and merge them
  """  
  # Create left and right lists
  left = arr[l:m+1]
  right = arr[m+1:r+1]

  # Create 3 pointers, one for left list, second for right list and third for main list
  i = 0     
  j = 0     
  k = l      
  # iterated both the lists and find the minimum element, place that on the kth index
  while i < len(left) and j < len(right) : 
      if left[i] <= right[j]: 
          arr[k] = left[i] 
          i += 1
      else: 
          arr[k] = right[j] 
          j += 1
      k += 1

  # Check for the remaining lists and add them at kth position
  while i < len(left): 
      arr[k] = left[i] 
      i += 1
      k += 1

  while j < len(right): 
      arr[k] = right[j] 
      j += 1
      k += 1

# Code to print the list 
def printList(arr): 
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end="\n")  
  printList(arr) 
  mergeSort(arr) 
  print("Sorted array is: ", end="\n") 
  printList(arr) 
