# Time Complexity : Best and Average case: O(N*LogN) when partition happens approx from the middle that is position of pivot 
# element is mostly at the middle of the array.
# Worst Case: O(N**2) = O(N^2): When array is already sorted in Ascending or Descending Order. In this case partitions are very
# imbalanced. The number of partitions would be O(N). Also our partition function is already O(N). So overall Time complexity would be O(N**2)
# Space Complexity : O(N) for stack
# Did this code successfully run on Leetcode : Could not find on Leetcode
# Any problem you faced while coding this : Had to check which data structure we could use to eliminate recursion. Then realised it
# could easily be replaced by stack. Then I was able to implement it


# Your code here along with comments explaining your approach
# Approach is similar to quick sort as done in recursive. Just used stack to eliminate recursion. Stack would be storing my left portion
# and right portion indices.

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  idx = l - 1
  for j in range(l, h):
    if(arr[j] <= pivot):
      idx += 1
      arr[j], arr[idx] = arr[idx], arr[j]

  idx += 1
  arr[h], arr[idx] = arr[idx], arr[h]
  return idx


def quickSortIterative(arr, l, h):
  #write your code here
  if(l < h):
    stack = [(l, h)]
    while(stack):
      low, high = stack.pop()
      pIndex = partition(arr, low, high)

      if(pIndex - 1 > low):
        stack.append((low, pIndex - 1))

      if(pIndex + 1 < high):
        stack.append((pIndex + 1, high))




# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [6, 5, 4, 3, 2, 1]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [7, 8, 9, 10, 11, 12, 13]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [7, 7, 7, 7, 7, 7]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = []
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")