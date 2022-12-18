# Exercise_5 : Iterative Quick Sort

# Average-Case Time Complexity: O(N log N), N = number of elements in array
# Worst-Case Time Complexity: O(N^2), N = number of elements in array
# Space Complexity: O(N), N = number of elements in the stack
# Successful Run on Leetcode: Yes (https://leetcode.com/problems/sort-an-array/)
# Challenges: None

def partition(arr, l, h):
  # partition the array using the last element as the pivot
  pivot = arr[h]
  # set the index of the smaller element to the left of the pivot
  i = l - 1
  # iterate through the array
  for j in range(l, h):
    # if the current element is smaller than the pivot
    if arr[j] < pivot:
      # increment the index of the smaller element
      i += 1
      # swap the current element with the element at the index of the smaller element
      arr[i], arr[j] = arr[j], arr[i]
  # swap the element at the index of the smaller element with the pivot
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  # return the index of the pivot
  return i + 1

def quickSortIterative(arr, l, h):
  # create a stack
  stack = []
  # push the initial values of l and h to the stack
  stack.append(l)
  stack.append(h)
  # keep popping the stack until it is empty
  while stack:
    # pop the stack
    h = stack.pop()
    l = stack.pop()
    # set the pivot
    p = partition(arr, l, h)
    # if the pivot is greater than 1, push the left and right subarrays to the stack
    if p - 1 > l:
      stack.append(l)
      stack.append(p - 1)
    if p + 1 < h:
      stack.append(p + 1)
      stack.append(h)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print(arr[i])