'''
Time Complexity : O(n^2) when elements are already sorted(worst/rare cases) other than that O(nlogn).
Space Complexity : O(logn).
Did this code successfully run on Leetcode : I can only find #912 - sort an array. but this problem cannot be solved with quick sort. This sol results in TLE.
Any problem you faced while coding this : went thought youtube video/blog on quick sort algo for once prior to coding it out to recall.
'''

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = l-1
  pivot = arr[h]
  for j in range(l,h):
    if arr[j] <= pivot:
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i + 1

def quickSortIterative(arr, l, h):
  # using stk to solve this iteratively.
  stk = []
  stk.append((l,h))
  while stk:
    l,h  = stk.pop()
    partitionFound = partition(arr,l,h)

    if partitionFound -1 > l:
      stk.append((l,partitionFound -1))

    if partitionFound + 1 < h:
      stk.append((partitionFound + 1, h))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i])
