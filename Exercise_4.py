# Python program for implementation of MergeSort 

# Time complexity - O(n * log n)
# Space complexity - O(n) 
#from turtle import left


def mergeSort(arr):
  if len(arr) > 1:
    leftArray = arr[:len(arr)//2]
    rightArray = arr[len(arr)//2:]

    #recursive calls
    mergeSort(leftArray)
    mergeSort(rightArray)
    
    #merge
    i = 0 # left array iterator
    j = 0 # right array iterator
    k = 0 # merged array iterator

    while i < len(leftArray) and j < len(rightArray):
      if leftArray[i] < rightArray[j]:
        arr[k] = leftArray[i]
        i += 1
      else:
        arr[k] = rightArray[j]
        j += 1
      k += 1

    #if elements are left in left array
    while i < len(leftArray):
      arr[k] = leftArray[i]
      i += 1
      k += 1

    #if elements are left in right array
    while j < len(rightArray):
      arr[k] = rightArray[j]
      j += 1
      k += 1
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
    print(arr[i], end = " ")
  print("")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end=" ")  
  printList(arr) 
  mergeSort(arr) 
  print("Sorted array is: ", end=" ") 
  printList(arr) 
