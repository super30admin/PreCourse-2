# Python program for implementation of MergeSort 

# // Time Complexity : O(n lg n) where n is the number of elements in the array
  # // Space Complexity : O(n) where n is the number of elements in the array 
  # for which recursive calls were made
  # // Did this code successfully run on Leetcode : yes
  # // Any problem you faced while coding this : a little when writing the 'terminating condition'
  # if l > r:
  #       return -1

  # // Your code here along with comments explaining your approach

def merge(left,right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
            res.append(left[i])
            i += 1
      else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
          res.append(left[i])
          i += 1
    
    while j < len(right):
          res.append(right[j])
          j += 1
    
    return res

def mergeSort(arr):
    if len(arr) < 2:
          return
    n = len(arr)
    # if n % 2 == 0:
    #   left = [0 for i in range(n//2)]
    #   right = [0 for i in range(n//2)]
    # else:
    #   left = [0 for i in range(n//2)]
    #   right = [0 for i in range((n//2) + 1)]
    left = []
    right = []

    i = 0 
    while i < n//2:
      left.append(arr[i])
      i += 1
    
    while i < len(arr):
      right.append(arr[i])
      i += 1

    mergeSort(left)
    mergeSort(right)
    return merge(left,right)
    
      
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
          print(arr[i],", ",end='')
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
