# Python code to implement iterative Binary  
# Search.
# It returns location of x in given array arr  
# if present, else returns -1
"""
Time Complexity : Worst Case O(logn) when value is at the extreme of the list;
Best Case O(1) when element present at the center
Space Complexity : O(log n)-- i cant figure out space complexity most of the times; need to go through
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this :
Your code here along with comments explaining your approach:
We check for the base exit condition right index(index of the last value) is greater than or equal to left index(initial value of 0)
We use recursive approach to solve this question. We find the midpoint of the list and the first condition we will check if
the element to be found is present at the middle position, if it is present at the middle position, we return the midpoint at which point
our algorithm will be fastest with complexity O(1) else, we check if the element to be found is less than the arr[midpoint], if it is then
we search the element in the left half of the list and keep on checking the element by redifining the left index as the initial 0 and and right index as midpoint-1
else we will repeat binary search with left index as midpoint+1 and right index as the last element of the list. In any case, midpoint will be the answer
"""


def binarySearch(arr, l, r, x):
  if r>=l:
      midpoint=l+r//2
      # print("midpoiint is", midpoint)
      if arr[midpoint]==x:
          return midpoint
      elif x<arr[midpoint]:
          return binarySearch(arr, l, midpoint-1, x)
      else:
          return binarySearch(arr, midpoint+1, r, x)
  else:
      return -1



# Test array
arr = [-1,0,3,5,9,12]
print(arr)
x = 2

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
