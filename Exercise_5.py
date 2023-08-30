#  Time Complexity : Average case: O(nlog(n)) Worst Case: O(n^2) 
#  Space Complexity : O(n) Size of the stack in iteration.
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[l]
  i = l
  j = h
  while(i<j):
      # increment i until arr[i] > pivot
      while(arr[i] <= pivot and i< h): 
          i += 1
      # decrement j until arr[i] <= pivot
      while(arr[j] > pivot and j> l):
          j -= 1
      
      # swap i and j position elements if i and j have crossed.
      if (i<j):
          arr[i],arr[j] = arr[j],arr[i]
      
      # repeat till i becomes greater than j
  # swap pivot and element at j.
  arr[l],arr[j] = arr[j],arr[l]
  return j  # return position which has been fixed.



def quickSortIterative(arr, l, h):
  s = []
  s.append(l)
  s.append(h)
  
  while(len(s)!=0):
    h = s.pop()
    l = s.pop()
    p = partition( arr, l, h )
    if (p-1 > l):
       # If there are elements on left side of pivot, then push left side low and high index to stack.
      s.append(l)
      s.append(p-1)
    if (p + 1 < h):
      # If there are elements on right side of pivot, then push right side low and high index to stack.
      s.append(p+1)
      s.append(h)
      
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
