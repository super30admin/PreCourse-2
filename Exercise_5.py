# Python program for implementation of Quicksort
# Time Complexity : O(n) = n log n
# Space Complexity : O(n) = n
# Did this code successfully run on Leetcode : I did not try. Will do soon.
# Any problem you faced while coding this : No, I had revised the partition method during previous problem.


# Your code here along with comments explaining your approach

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l
  for j in range(l, h):
    if arr[h] >= arr[j]:
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp
      i+=1
  temp = arr[i]
  arr[i] = arr[h]
  arr[h] = temp
  return i


def quickSortIterative(arr, l, h):
  #write your code here
  quick_stack = [(l, h)]
  while len(quick_stack) > 0:
    top = quick_stack.pop()
    if top[0] < top[1]:
      mid = partition(arr, top[0], top[1])
      quick_stack.append((top[0], mid-1))
      quick_stack.append((mid+1, top[1])) 

# Driver code to test above 
arr = [10, 9, 8, 7, 6, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 



