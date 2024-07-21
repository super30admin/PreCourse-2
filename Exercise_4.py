# Python program for implementation of MergeSort 
# Time Complexity : O(n*logn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def merge(arr, l,mid,h):
    # merge arr1: (l,mid) and arr2:(mid+1,h)
    len1 = mid - l + 1
    len2 = h - mid
    i, j = 0, 0
    k = l
    a1 = [0]*(len1)
    a2 = [0]*(len2)
    while i < len1:
       a1[i] = arr[i+l]
       i += 1
    while j < len2:
       a2[j] = arr[j+mid+1]
       j += 1
    # merged = []
    i, j = 0,0
    while i < len1 and j < len2:
      if a1[i] < a2[j]:
        arr[k] = a1[i]
        i += 1
        k += 1
      else:
          arr[k] = a2[j]
          j += 1
          k += 1
    while i < len1:
      arr[k] = a1[i]
      i += 1
      k += 1
    while j < len2:
      arr[k] = a2[j]
      j += 1
      k += 1
    


def mergeSort(arr, l, h):
    if l < h:
      mid = (l + h - 1)//2
      mergeSort(arr, l, mid)
      mergeSort(arr, mid + 1, h)
      merge(arr, l, mid, h) # merge (l to mid) and (mid+1 to h)
  
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
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
