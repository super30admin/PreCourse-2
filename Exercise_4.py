#Time Complexity : O(N*logN)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) >1:
    i=j=k=0
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeSort(L)
    mergeSort(R)
    while i < len(L) and j < len(R) :  
      if L[i] < R[j]:
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
    for each in arr:
      print(each)
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
