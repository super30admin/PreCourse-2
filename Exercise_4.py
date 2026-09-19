# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  # Base case:
  # One element is already sorted
    if len(arr) > 1:

      # Find middle
      mid = len(arr) // 2

      # Divide array into two halves
      left = arr[:mid]
      right = arr[mid:]

      # Sort left half
      mergeSort(left)

      # Sort right half
      mergeSort(right)

      # i = index for left
      # j = index for right
      # k = index for original array
      i = 0
      j = 0
      k = 0

      # Compare elements from left and right
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          arr[k] = left[i]
          i += 1
        else:
          arr[k] = right[j]
          j += 1
        k += 1
      # Copy remaining left elements
      while i < len(left):
         arr[k] = left[i]
         i += 1
         k += 1
      # Copy remaining left elements
      while j < len(right):
         arr[k] = right[j]
         j += 1
         k += 1
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
       print(arr[i], end=" ")

    print()

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
