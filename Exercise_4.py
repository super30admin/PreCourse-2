# Python program for implementation of MergeSort 
import math
def mergeSort(arr):
  #write your code here
  
  merged_arr = [-1 for x in range(len(arr))]

  def merge(l, mid, r): #O(n) = n log n
    if l == r:
      merged_arr[l] = arr[l]
      return
    i, j = 0,0
    k=l
    temp_l = merged_arr[l:mid+1]
    temp_r = merged_arr[mid+1:r+1]
    while i < len(temp_l) and j < len(temp_r):
      if temp_l[i] <= temp_r[j]:
        merged_arr[k] = temp_l[i]
        i+=1
      else:
        merged_arr[k] = temp_r[j]
        j+=1
      k+=1
    while i < len(temp_l):
      merged_arr[k] = temp_l[i]
      i+=1
      k+=1
    while j < len(temp_r):
      merged_arr[k] = temp_r[j]
      j+=1
      k+=1

  def divide(l, r): #O(n) = log(n)
    mid = int(math.floor((l+r)/2))
    if l < r:
      divide(l, mid)
      divide(mid+1, r)
    merge(l, mid, r)
  
  divide(0, len(arr)-1)
  for x in range(0, len(merged_arr)):
    arr[x] = merged_arr[x]
  
# Code to print the list 
def printList(arr): 
    for e in arr:
      print(e, end=" ")
    print()
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
