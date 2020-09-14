# Python program for implementation of Quicksort

class Stack():
  def __init__(self, size):
    self.stack = [0]*size
    self.top = -1
  def push(self, item):
    self.top += 1
    self.stack.append(item)  
  def pop(self):
    if(self.top>-1):
      self.top -= 1
      return self.stack.pop()  
    return None
  def get_top(self):  
    return self.top

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot_index = h
  i = l-1
  for j in range(l, pivot_index):
      if(arr[j]>arr[pivot_index]):
          continue
      else:
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]
  return i+1

def quickSortIterative(arr, l, h):
  # Time Complexity : O(n log n)
  # Space Complexity : O(log n) for the stack
  # In this approach we are using an auxiliary stack instead of using recursion, the low, high indices are stored, partition is called on each halves   
  #write your code here
  stack = Stack(len(arr))
  stack.push(l)
  stack.push(h)

  while(stack.get_top()>-1):
    h = stack.pop()
    l = stack.pop()

    p = partition(arr, l, h)

    if(p-1>l):
      stack.push(l)
      stack.push(p-1)

    if(p+1<h):
      stack.push(p+1)
      stack.push(h)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print(arr)