# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
'''
my output:
komalbhavake$ python3 Exercise_5.py
Given array is: [10, 7, 8, 9, 1, 5]
Sorted array is: [1, 5, 7, 8, 9, 10]
'''
# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l,h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i + 1] , arr[h] = arr[h] , arr[i + 1]
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l,h)]

  while stack:
    start, end = stack.pop()
    p = partition(arr, start, end)

    if p - 1 > start:
      stack.append((start, p - 1))
    
    if p + 1 < end:
      stack.append((p + 1, end))

# driver code to test the above code 
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Given array is:", arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:", arr)
