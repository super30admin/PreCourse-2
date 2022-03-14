# Time Complexity : θ(n log(n))  
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : No
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort 
def mergeSort(arr):

  if len(arr) > 1:
      
      mid = len(arr) // 2
      left = arr[:mid]
      right = arr[mid:]

      # Recursive call on each half
      mergeSort(left)
      mergeSort(right)

      # Two iterators for traversing the two halves
      i = 0
      j = 0
      
      # Iterator for the main list
      k = 0
      
      while i < len(left) and j < len(right):
          if left[i] <= right[j]:
            # The value from the left half has been used
            arr[k] = left[i]
            # Move the iterator forward
            i += 1
          else:
              arr[k] = right[j]
              j += 1
          # Move to the next slot
          k += 1

      # For all the remaining values
      while i < len(left):
          arr[k] = left[i]
          i += 1
          k += 1

      while j < len(right):
          arr[k]=right[j]
          j += 1
          k += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
      print(arr[i])
  
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ") 
    printList(arr)


    