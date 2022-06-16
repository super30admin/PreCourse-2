# Python program for implementation of Quicksort
# Time Complexity : O(n*log n)
# Space Complexity : O(log n) as partition done similar to tree
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : None
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  p = arr[l] # considering l element as p
  left = l + 1
  right = h
  while True:
      while left <= right and arr[left] <= p:  # while left element is less than or equal to right and less than or equal to p element
          left += 1
      while left <= right and arr[right] >= p: # while right element is greater than or equal to left and greater than or equal to p element
          right -= 1
      if right < left: # loop breaks when right element becomes less than left
          break
      else:
          arr[left],arr[right] = arr[right],arr[left] # initialising left to right and vice-versa
  arr[l],arr[right] = arr[right],arr[l]
  return right

def quickSortIterative(arr, l, h):
  #write your code here
  # creating an empty stack
  length_of_stack = (h - l) + 1
  stack = [0] * (length_of_stack)

  #initialising top of the stack to -1 denoting it as empty
  top = -1

  #pushing initial values of low and high to stack
  top += 1 # incrementing top value by 1
  stack[top] = l # added low value to stack's top
  top += 1
  stack[top] = h

  # keep removing from stack if its not empty
  while top >= 0: # checking if top value is greater than or equal to zero
      h = stack[top]
      top -= 1
      l = stack[top]
      top -= 1

      pivot = partition(arr,l,h) # choosing the pivot element's index

      # pushing left side elements to stack
      if pivot - 1 > l:
          top += 1
          stack[top] = l
          top += 1
          stack[top] = pivot - 1

      # pushing right side of elements to stack
      if pivot + 1 < h:
          top += 1
          stack[top] = pivot + 1
          top += 1
          stack[top] = h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print(f"Original array is: {arr} ")
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
print(arr)
