# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
# We divide the arr into two halves, sort them separately and 
# merge the sorted halves

# Python program for implementation of MergeSort 
def mergeSort(arr):

  #write your code here
  if len(arr) > 1:
    l = 0
    r = len(arr) - 1
    mid = (l+r)//2
    L = arr[:mid]  #dividing arr into two halves
    R = arr[mid:]

    mergeSort(L)   #sorting them again
    mergeSort(R)

    #for three diff arr, we use three diff index to keep track
    i = 0  #for L
    j = 0  #for R
    k = 0  #for arr
    while i < len(L) and j < len(R):    #merge them after comparing
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    #if L has no more elements, but R does
    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
    
    #if R has no more elements, but L does
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1


# Code to print the list 
def printList(arr): 

    #write your code here
    for i in range(len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
