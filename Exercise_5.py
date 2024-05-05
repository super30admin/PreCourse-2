# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(array, low, high):
  pivot = array[high]
  i = low-1

  for j in range(low, high):
    if array[j] <= pivot:
      i+=1 
      array[i], array[j] = array[j], array[i]
  
  array[i+1] , array[high] = array[high] , array[i+1]
  return i+1

def quickSortIterative(arr, low, high):
  stack = []
  stack.append((low, high))

  while stack :
    low, high = stack.pop()

    if low < high:
      pi = partition(arr, low, high)

      stack.append((low, pi-1))
      stack.append((pi+1, high))


# Driver code to test above 
# this looks like in place sorting! 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 