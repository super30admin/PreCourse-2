# Python program for implementation of Quicksort
# Time Complexity: Avg Case: O(nlog(n)) | Worse Case: O(n^2)(When the array is in descending order)
# Space Complexity: O(log(n)) for the queue

# give you explanation for the approach
# - So during partition we choose a pivot and segregate the array in such a way that values smaller than
#   the pivot are added to the left side and values grater, to the right. 
# - To acheive this we have a variable i, which is used to keep track of the last element that is smaller than the pivot. 
#   So if we find a smaller value during our iteration, we swap with the ith element.
# For the iterative approach, instead of recursion you can use a queue to keep track of the partition indexes 

from collections import deque

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
      if arr[j] < pivot:
          i += 1
          temp = arr[j]
          arr[j] = arr[i]
          arr[i] = temp
  
  temp = arr[i + 1]
  arr[i + 1] = arr[h]
  arr[h] = temp
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  
  queue = deque([(l, h)])

  while len(queue) > 0:

    l, h = queue.popleft()
    if l >= h:
      continue

    mid = partition(arr, l, h)

    queue.append([l, mid - 1])
    queue.append([mid + 1, h])

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is: " + str(arr))

