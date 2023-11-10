# Time Complexity: 
# Space Complexity:
# Is this problem on leetcode: Dont know
# Problem faced while solving? : Was confused in the stack part .

# Code along with comments

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = (l - 1)
  x = arr[h]

  for j in range(l, h):
    if arr[j] <= x:

      i = i + 1                                     # Increment index of smaller element
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)

def quickSortIterative(arr, l, h):                  # Fuction to do quickSort using the iteraive method

  size = h - l + 1        
  stack = [0] * (size)                              # Create a stack of size equal to list

  top = -1                                          # Initailize the stack

  top = top + 1                                     # push elements one by one in stack 
  stack[top] = l
  top = top + 1
  stack[top] = h

  while top >= 0:                                   # Not empty pop
    h = stack[top]                                  # Pop h
    top = top - 1
    l = stack[top]                                  # Pop l
    top = top - 1

    p = partition(arr, l, h)                        # Partition used for sorting

    if p-1 > l:                                     # This will push elements to the left of partition
      top = top + 1
      stack[top] = l
      top = top + 1
      stack[top] = p - 1

    if p + 1 < h:                                   # This will push elements to the right of partition
      top = top + 1
      stack[top] = p + 1
      top = top + 1
      stack[top] = h

arr = [4,3,5,2,1,3,2,3]                             # Driver code
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
  print("%d" % arr[i]),
