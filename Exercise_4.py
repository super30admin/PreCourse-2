#  Time Complexity : O(nlogn)
#  Space Complexity : O(n)
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No
# Python program for implementation of MergeSort

def merge(a,b,arr):
  # a and b are two sub lists which are to be merged.
  i = 0
  j = 0
  k = 0
  while(i< len(a) and j < len(b)): # until i or j reaches end of their respective lists.
    if(a[i]<=b[j]):
      arr[k] = a[i]
      k += 1
      i += 1
    else:
      arr[k] = b[j]
      k += 1
      j += 1
  # add remaining elements from either a or b to the resultant list.
  while(i<len(a)):
    arr[k] = a[i]
    i += 1
    k += 1
  while(j<len(b)):
    arr[k] = b[j]
    j += 1
    k += 1

def mergeSort(arr):
  # Split at the middle and recursively call mergeSort until each we get a list of single element.
  if(len(arr) > 1):
    mid = len(arr)//2
    left_array = arr[:mid]
    right_array = arr[mid:]
    mergeSort(left_array)
    mergeSort(right_array)
    merge(left_array,right_array,arr)
  
# Code to print the list 
def printList(arr):
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
