# Python program for implementation of MergeSort
"""
In merge sort we divide the array into half which will be the mid pointer
we use mid pointer to split the array into two half left and right 
again we do the same until the length become 1 from the we will have pointer for i,j and k
i is left_half and j is for right_half
we compare the values of ith and jth element
we insert at the kth index to the original array
at the end we porcess the remaining length
incrementing the pointer at each step
time complexity O(n long n)
space comlexity O(n) 
"""
def mergeSort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    mergeSort(left_half)
    mergeSort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):

      if left_half[i] <= right_half[j]:
        arr[k] = left_half[i]
        i += 1
        k +=1
      else:
        arr[k] = right_half[j]
        j += 1
        k += 1
    

    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1
    
    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    for a in arr:
      print(a)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
