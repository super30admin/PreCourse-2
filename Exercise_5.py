# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot, pivot_idx = arr[l], l
    l = l+1
    while l < h:
        while l < len(arr) and arr[l] <= pivot:
            l += 1
        while arr[h] > pivot:
            h -= 1
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]
    arr[h], arr[pivot_idx] = arr[pivot_idx], arr[h]
    return h

'''
Instead of using recursion stackspace, we create our own auxiliary stack to avoid recursion calls
'''
def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l, h)]
  while stack:
    low, high = stack.pop()
    if low < high:
      pi = partition(arr, low, high)
      stack.append((low, pi-1))
      stack.append((pi+1, high))
  return arr

# Driver code to test above 
arr = [10 , 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

'''
Time complexity: O(N^2) - worst case when every time we pick the smallest elem as pivot i.e. array is already sorted
Average time complexity (for randomly shuffled array) - O(NlogN)

Space complexity: O(N) - all the possible partitioned subarray indexes may be placed in the stack
'''