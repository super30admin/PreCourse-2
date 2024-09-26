"""Time Complexity : O(nLogn)
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : I had difficulty visualizing 
the recursion.
"""
# Python program for implementation of MergeSort 
def mergeSort(arr):
  #checking if array contains more than 1 elements
  if len(arr) > 1:
    #finding midpoint to divide array
    mid = len(arr)//2
    #left half of the array
    left = arr[:mid]
    #right half of the array
    right = arr[mid:]

    #applying recursive mergeSor on left halves and right halves
    mergeSort(left)
    mergeSort(right)

    #initializing indexes to start the merge
    leftLIndex = rightLIndex = finalLIndex = 0

    #swapping and merging the arrays
    while leftLIndex < len(left) and rightLIndex < len(right):
      if left[leftLIndex] < right[rightLIndex]:
        arr[finalLIndex] = left[leftLIndex]
        leftLIndex += 1
      else:
        arr[finalLIndex] = right[rightLIndex]
        rightLIndex += 1
      finalLIndex += 1

    #Now after arranging let's fill the remaining elements
    while leftLIndex < len(left):
      arr[finalLIndex] = left[leftLIndex]
      leftLIndex += 1
      finalLIndex += 1 
    while rightLIndex < len(right):
      arr[finalLIndex] = right[rightLIndex]
      rightLIndex += 1
      finalLIndex += 1 
  
# Code to print the list 
def printList(arr):
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
