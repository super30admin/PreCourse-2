# Python program for implementation of Quicksort
"""
TC: O(N^2) for worst-case
    O(NlogN) for average case
SC: O(N) (if we consider recrusion stack as a memory in worst-case)

Similar approach to recursive, just replaced the recrusion calls to a stack
"""

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l] #choosing the element @ low
  i, j = l, h

  while True:
    while arr[i] < pivot:
      i += 1

    while arr[j] > pivot:
      j -= 1
    
    if i >= j: #when they both cross each other
      return j
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1



def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l,h)]

  while stack:
    low, high = stack.pop()
    if low < high:
      j = partition(arr, low, high)

      stack.append((low, j))
      stack.append((j+1, high))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i]) 

