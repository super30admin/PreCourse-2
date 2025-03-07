# Python program for implementation of MergeSort 
#Time complexity:Best -> O(n logn) Worst -> O(n logn)
#Space complexity:Best -> O(n) Worst -> O(n)
def mergeSort(arr):
  
  #write your code here
  #we recursively divides the array into halves, sorts each half,and then merges them back together in sorted order.
  if len(arr) > 1: #afterc finding middle index, we divided the arrays
    midpoint = len(arr)//2
    leftarr = arr[:midpoint]
    rightarr = arr[midpoint:]

    #sorting both halves recursively
    mergeSort(leftarr) 
    mergeSort(rightarr)
    #pointer for lrft, right and original array
    i = 0
    j = 0
    k = 0

    while (i < len(leftarr)) and (j < len(rightarr)):
      #if left element is smaller
      if leftarr[i] <= rightarr[j]:
          arr[k] = leftarr[i]
          i += 1
      else:
          #if left element is smaller
          arr[k] = rightarr[j]
          j += 1
      k += 1 

    while i < len(leftarr):  # Copy remaining elements of leftarr if present
      arr[k] = leftarr[i]
      i += 1
      k += 1

    while j < len(rightarr):  # Copy remaining elements of rightarr if present
      arr[k] = rightarr[j]
      j += 1
      k += 1
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
