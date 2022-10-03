# Python program for implementation of Quicksort Sort 
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Any problem you faced while coding this :no
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    #divide the array in 2 halves left and right
    mid = len(arr) // 2
    arr_L = arr[:mid]
    arr_R = arr[mid:]

    #Sorting the two halves
    mergeSort(arr_L)
    mergeSort(arr_R)

    l, r, m = 0, 0, 0

    while l < len(arr_L) and r < len(arr_R):
      if arr_L[l] < arr_R[r]:
        arr[m] = arr_L[l]
        l +=1
      else:
        arr[r] = arr_R[r]
        r += 1
      m +=1 

    #when elements from arr_L and arr_R are exhausted then put back in arr 
    while l < len(arr_L):
      arr[m] = arr_L[l]
      l +=1
      m +=1

    while r < len(arr_R):
      arr[m]  = arr_R[r]
      r += 1
      m += 1
  
# Code to print the list 
def printList(arr):
  for i in range(len(arr)):
    print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
