# Time Complexity : O(n log(n)). Partitioning step takes linear time, and on average it is called log(n) times.
# total time complexity if of the order of n * log(n)

# Space Complexity : O(log(n)) The maximum size of the stack is equal to the number of splits, which is log(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  
  mid = (l+h)//2
  pivot = arr[mid]
  while l <= h:
    # Update left pointer to first element that is greater than the pivot, starting at beginning of the array
    while arr[l] < pivot:
      l+=1 
    # Update right pointer to first element that is smaller than the pivot, starting at end of the array
    while arr[h] > pivot:
      h-=1
    # Swap elements at l and h pointers if l < h
    if l <= h:
      arr[h], arr[l] = arr[l], arr[h]
      h-=1
      l+=1
  # Return correct position of pivot element in the sorted array
  return l

def quickSortIterative(arr, l, h):
  #write your code here
  # A stack can be used to replace the recursive calls
  stack = []
  # Initialize the stack with starting and ending indices on the array
  stack.append((l, h))

  while stack:
    # Pop top most element from the stack
    low, high = stack.pop()
    if low < high:
      # Partition the array and get the pivot index
      pivot_index = partition(arr, low, high)

      # Append indices of left and right sub arrays of the array
      
      stack.append((low, pivot_index - 1))
      stack.append((pivot_index, high))



# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 