# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  pivot = arr[h]

  i = l - 1

  for j in range(l, h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1


def quickSortIterative(arr, l, h):
  #write your code here

  stack = [(l, h)]

  while stack:
    low, high = stack.pop()

    if low < high:
      pi = partition(arr, low, high)

      if pi + 1 < high:
        stack.append((pi + 1, high))
      
      if low < pi - 1:
        stack.append((low, pi - 1))
  
  return arr

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

