# Time Complexity :O(n log N)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :No 
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)>1:
    m=len(arr)//2
    left=arr[:m]
    right=arr[m:]
    mergeSort(left)
    mergeSort(right)
    i=0
    j=0
    k=0
    while i<len(left) and j <len(right):
      if left[i]<right[j]:
        arr[k]=left[i]
        i=i+1
      else:
        arr[k]=right[j]
        j=j+1
      k=k+1

    while i<len(left):
      arr[k]=left[i]
      i=i+1
      k=k+1
    while j<len(right):
      arr[k]=right[j]
      j=j+1
      k=k+1
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in range(len(arr)):
    print(arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
