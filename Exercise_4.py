'''
Time Complexity : O(n log n), where n is elements in array
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach: creating partitions and merging
'''
# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  length = len(arr)
  if length>1:
     mid = length//2
     partA = arr[:mid]
     partB = arr[mid:]
     mergeSort(partA)
     mergeSort(partB)

     i = j = 0
     k = 0
     n = len(partA)
     m = len(partB)
     
     while i < n and j<m:
        if partA[i] <= partB[j]:
           arr[k]=partA[i]
           i+=1
           k+=1
        else:
           arr[k]=partB[j]
           j+=1
           k+=1
      
     while i<n:
        arr[k]=partA[i]
        k+=1
        i+=1

     while j<m:
        arr[k]=partB[j]
        j+=1
        k+=1
      
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in range(len(arr)):
       print(arr[i], end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print()
    print("Sorted array is: ", end="\n") 
    printList(arr) 
