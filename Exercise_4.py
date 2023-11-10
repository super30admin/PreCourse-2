
# Python program for implementation of MergeSort 
# // Time Complexity : O(nlog n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2

    left_array = arr[ : mid]
    right_array = arr[mid : ]

    mergeSort(left_array)
    mergeSort(right_array)

    i=j=k=0

    while i < len(left_array) and j < len(right_array):
      if left_array[i] < right_array[j]:
        arr[k] = left_array[i]
        i += 1
      else:
        arr[k] = right_array[j]
        j += 1 
      k += 1

    while i < len(left_array):
      arr[k] = left_array[i]
      k += 1
      i += 1

    while j < len(right_array):
      arr[k] = right_array[j]
      k += 1
      j += 1


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
