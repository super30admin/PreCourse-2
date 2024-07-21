# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]
  i = l + 1
  for j in range(l+1, h+1):
    if (arr[j] < pivot):
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[l], arr[i-1] = arr[i-1], arr[l]
  return i-1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l,h)]
  
  while stack:
    l,h = stack.pop()
    pivot = partition(arr, l, h)
    if (pivot - 1) > l: # if elements present on the left
      stack.append((l,pivot-1))
    elif (pivot + 1) < h:
      stack.append((pivot+1,h))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 