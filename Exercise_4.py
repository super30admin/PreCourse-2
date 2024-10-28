# Python program for implementation of MergeSort 
def merge(arr, l, m, r):
  # Create temporary arrays
  left = arr[l:m + 1]
  right = arr[m + 1:r + 1]

  i = j = 0  # Initial index of left and right subarrays
  k = l      # Initial index of merged array

  # Merge the temporary arrays back into arr[l..r]
  while i < len(left) and j < len(right):
      if left[i] <= right[j]:
          arr[k] = left[i]
          i += 1
      else:
          arr[k] = right[j]
          j += 1
      k += 1

  # Copy the remaining elements of left[], if any
  while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1

  # Copy the remaining elements of right[], if any
  while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1


def mergeSort(arr, l, r):
  #write your code here
  if l < r:
    m = (l + r) // 2

    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)

    merge(arr, l, m, r)

  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
