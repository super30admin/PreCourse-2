# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(low, high):
  #write your code here
  mid = (low + high)//2
  left = low
  pivot = arr[mid]
  arr[high], arr[mid] = arr[mid], arr[high]

  for i in range(low, high):
    if arr[i] < pivot:
      arr[left], arr[i] = arr[i], arr[left]
      left += 1
  arr[left], arr[high] = arr[high], arr[left]
  return left

def quickSortIterative(low, high):
  #write your code here
  stack = [(low, high)]

  while stack:
    cur_low, cur_high = stack.pop()
    item = partition(cur_low, cur_high)

    if item>cur_low:
      stack.append((cur_low,item-1))
    
    if item < cur_high:
      stack.append((item+1, cur_high))
    
arr = [10, 80, 30, 90, 40, 50, 70]

print("before: ", arr)
quickSortIterative(0, len(arr)-1)
print("after: ", arr)
