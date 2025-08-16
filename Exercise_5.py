# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  i = (l - 1)  # index of smaller element
  pivot = arr[h]  # pivot
  for j in range(l, h):
    # If current element is smaller than or equal to pivot
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]  # swap

  arr[i + 1], arr[h] = arr[h], arr[i + 1]  # swap
  return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  myst = []
  myst.append((l, h))
  while myst:
    l, h = myst.pop()
    if l < h:
      pi = partition(arr, l, h)
      myst.append((l, pi - 1))
      myst.append((pi + 1, h))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
