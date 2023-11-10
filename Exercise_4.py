'''
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Had to revise the concepts once 

We split the array into two arrays using a mid, then we sort those smaller arrays
After that we merge our 2 sorted arrays into one
'''
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)<=1:
    return 
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  mergeSort(left)
  mergeSort(right)
  mergeSortedArrays(left,right,arr)

def mergeSortedArrays(arr_a,arr_b,arr):
  len_a=len(arr_a)
  len_b=len(arr_b)
  i=j=k=0
  while i<len_a and j<len_b:
    if arr_a[i]<=arr_b[j]:
      arr[k]=arr_a[i]
      i+=1
    else:
      arr[k]=arr_b[j]
      j+=1
    k+=1
  #Incase any of the above condition is true, add remaining elements to the sorted list
  while i < len_a:
    arr[k]=arr_a[i]
    i+=1
    k+=1
  while j < len_b:
    arr[k]=arr_b[j]
    j+=1
    k+=1
# Code to print the list 
def printList(arr): 
  print(arr)
  
#driver code to test the above code 
if __name__ == '__main__':
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end="\n")  
  printList(arr) 
  mergeSort(arr) 
  print("Sorted array is: ", end="\n") 
  printList(arr) 
