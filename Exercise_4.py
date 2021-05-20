# Python program for implementation of MergeSort 
# Time Complexity: nlog(n)
# Space Complexity: O(n)
# Approach: 
# 1.Find the mid element of the array and divide the array in two parts. 
# 2.Call mergeSort recursively for left and right subparts.
# 3.Take another array and insert elements in it by traversing both the arrays. 
# 4.If element in left subarray is smaller, insert that in new array otherwise insert element from right subarray.
# 5.If any of the subarray has elements still left in it, put them into the new array.

def mergeSort(arr):
  if len(arr) > 1:

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
      if L[i] <  R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
      print(arr[i], end = " ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
