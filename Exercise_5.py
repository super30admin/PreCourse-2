# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]  # Choosing the last element as the pivot
  i = l - 1  # Pointer for the smaller element
  for j in range(l, h):
      # If the current element is smaller than or equal to the pivot
      if arr[j] <= pivot:
          i += 1
          # Swap the found smaller element with the element at i
          arr[i], arr[j] = arr[j], arr[i]

  # Swap the pivot element with the element at i+1
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l, h))
  while stack:
    i, j = stack.pop()
    if i < j:
        pivot = partition(arr, i, j)
        stack.append((i, pivot - 1))
        stack.append((pivot + 1, j))
  return arr

# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr) 
new = quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %new[i]), 
