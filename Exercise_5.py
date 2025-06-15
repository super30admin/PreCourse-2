'''
1) partition()
Time complexity: O(N)
Space complexity: O(1)

2) quickSortIterative()
Time complexity: Best case O(NlogN) and worst case O(N^2)
Space complexity: Best case O(logN) and worst case O(N)
'''

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
   pivot_index = arr[h]
   i = l - 1 

   for j in range(l, h):
        if arr[j] <= pivot_index:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

   arr[i + 1], arr[h] = arr[h], arr[i + 1]
   return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l, h)] 
  while stack:
    l, h = stack.pop()
    if l < h:
      pivot_index = partition(arr, l, h)
      if pivot_index + 1 < h:
        stack.append((pivot_index + 1, h))
      if l < pivot_index - 1:
        stack.append((l, pivot_index - 1))


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
