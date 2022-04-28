# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

# Hi TA / Jaspinder, Is there any alternative to implement iterative quicksort without using a stack?

# Acts similar to the internal stack used in recursive procedures. We store the low and high indices of while partitioning the array

callstack = []

def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l, h):
    if arr[j] < pivot:
      i += 1
      arr[j], arr[i] = arr[i], arr[j]
  arr[i+1], arr[h] = arr[h], arr[i+1]

  return i+1


def quickSortIterative(arr):

  while callstack:
    low, high = callstack.pop()
    if low < high:
      p = partition(arr, low, high)
      callstack.append((p+1, high))
      callstack.append((low, p-1))
    


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
callstack.append((0, n-1)) 
quickSortIterative(arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 


