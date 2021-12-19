# Python program for implementation of Quicksort
# Time Complexity : O(nlog(n))
# Space Complexity : O(n), 
# Did this code successfully run on Leetcode : Yes,
# Any problem you faced while coding this : no


def partition(arr, low, high):
  #write your code here
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSortIterative(arr, l, h):
  #write your code here
  stacklist = []

  stacklist.append(l)
  stacklist.append(h)

  while stacklist:
      high=stacklist.pop()
      low=stacklist.pop()

      p=partition(arr,low, high) #gets the pivot element

      if p-1>low: #if elements are present on the left side of the pivot, we add the end points from low to p-1 to the stack
        stacklist.append(low)
        stacklist.append(p-1)

      if p+1<high: #if elements are present on the right side of the pivot, we add the end points from p+1 to high to the stack
        stacklist.append(p+1)
        stacklist.append(high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 