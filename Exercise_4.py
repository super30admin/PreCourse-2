'''
// Time Complexity : Best, Worst, Avg : O(N Log(N))
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Spent time on understanding the logic


// Your code here along with comments explaining your approach

'''
'''
Two functions:
  1. Recursively slices the array into half until array length is 1 - 
    - After this recursion would unfold : Call merge while recursion unfolds
  2. Merge : takes two arrays of any length and merges with sorted value
'''

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)==1:
    return arr
  mid=len(arr)//2
  left=arr[:mid]
  right=arr[mid:]
  return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
  result=[]
  i,j=0,0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      result.append(left[i])
      i+=1
    else:
      result.append(right[j])
      j+=1
  
  while i<len(left):
    result.append(left[i])
    i+=1
  while j<len(right):
    result.append(right[j])
    j+=1
  return result
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    print("Sorted array is: ", end="\n") 
    printList(mergeSort(arr) )
    
    
