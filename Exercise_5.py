'''
Time Complexity : O(n log n), where n is elements in array
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No
Your code here along with comments explaining your approach: choosing rightmost element as pivot.
instead of recurrsion, using stack to keep track of left and right index of the partitions.
'''

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  i = l

  for j in range(l, h):
    if arr[j]<=pivot:
      arr[j], arr[i] = arr[i], arr[j]
      i+=1
  
  arr[i], arr[h] = arr[h], arr[i]
  return i


def quickSortIterative(arr, l, h):
  #write your code here
  length = len(arr)
  stack = [0]*length
  stack.append(l)
  stack.append(h)
  top = 1 #after pushing 2 elements

  while stack:
    high = stack.pop()
    top-=1
    low = stack.pop()
    top-=1

    pivotIndex = partition(arr, low, high)

    if pivotIndex-1 > low:
      stack.append(low)
      stack.append(pivotIndex-1)
      top+=2
    
    if pivotIndex+1 < high:
      stack.append(pivotIndex+1)
      stack.append(high)
      top+=2


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i], end=" "), 