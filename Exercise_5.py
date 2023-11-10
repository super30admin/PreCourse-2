# Time Complexity : 
# Best Case: O(N(log(N))) 
# > Each partition breaks the input into halves. Acheiving logarithmic performance.
# > To achieve this partition all N elements must be visited. Hence, N * logN
# Worst Case: O(N^2) 
# Each partition picks the smallest or largest element. Breaking the input into 
# two parts, i.e., 1, N - 1 > Each partition must visit each element. Hence, N * (N - 1)

# Space Complexity : (Recursion Stack)
# Best Case Space Complexity = O(log (N)) 
# Worst Case Space Complexity = O(N)

# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : Spent some time visualising the stack and convincing myself of why it woud work.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  
  pivot = arr[l]
  left = l + 1
  right = h

  while left <= right:
    while left <= h and arr[left] < pivot:
      left += 1
    while right > l and arr[right] >= pivot:
      right -= 1
    if left < right:
      arr[left], arr[right] = arr[right], arr[left]
  arr[l], arr[right] = arr[right], arr[l]
  return right

def quickSortIterative(arr, l, h):
  '''Mimic the recursion stack'''

  stack = [[l,h]] # Initialise the stack
  while len(stack) != 0:
    curr = stack.pop() # Take call on top of stack.
    low = curr[0]
    high = curr[1]
    if low >= high:
      continue
    idx = partition(arr, low, high)
    stack.append([low, idx - 1]) # Push left sub-array call.
    stack.append([idx + 1, high]) # Push right sub-array call.



# Driver code to test above 
arr = [10, 7, 1,2, 3, 11, 13, 8, 9, 12, 5]
print("Original Array: {}".format(arr))
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is: {}".format(arr)) 
