#Time Complexity :  O(nlogn)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]  

    # Recursive call on each half
    mergeSort(left)
    mergeSort(right)

    # Two iterators for traversing the two halve parts
    i = 0
    j = 0
        
    # Main list iterator
    k = 0
    while i < len(left) and j < len(right):
      if left[i] >= right[j]:
        arr[k]=right[j]
        k=k+1
        j=j+1
      else:
        arr[k]=left[i]
        i=i+1
        k=k+1
    #remaining values on left array
    while i<len(left):
      arr[k]=left[i]
      k=k+1
      i=i+1
    #remaining values on right array
    while j<len(right):
      arr[k]=right[j]
      k=k+1
      j=j+1

# Code to print the list 
def printList(arr):
  for i in range(0,len(arr)):
    print(arr[i]) 
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 