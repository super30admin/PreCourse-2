# Python program for implementation of Quicksort

# Partition the array till the stack is empty by selecting a pivot. Bring all the values smaller than pivot to the left and greater than pivot to the right.
# Pop the first element in the stack everytime
# If p-1 is greater than low, push low and p-1 to the stack, if p+1 is less than high, push p+1 and high in the stack.
# Basically if we have left side to partition index, we put it in the stack and if we have right side to the partition index we put it in the stack.
# Do this till the stack is empty

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def partition(arr, l, h):
  pivot = arr[h]
  pIndex = l
  for i in range(l, h):
      if arr[i] <= pivot:
          arr[i], arr[pIndex] = arr[pIndex], arr[i]
          pIndex += 1
  arr[pIndex], arr[h] = arr[h], arr[pIndex]
  return pIndex 

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(l)
  stack.append(h)

  while stack:
    new_h = stack.pop()
    new_l = stack.pop()
    p = partition(arr, new_l, new_h)
    if p - 1 > new_l:
      stack.append(new_l)
      stack.append(p-1)
    if p+1 < new_h:
      stack.append(p+1)
      stack.append(new_h)
  print(arr)


arr = [10, 7, 8, 9, 1, 5, 4] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  