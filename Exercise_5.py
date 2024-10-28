# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot = arr[high]
  i, j = low, high
  while i < j:
      while arr[i]<= pivot and i < high:
          i += 1
      
      while arr[j]>= pivot and j > -1:
          j -= 1
      
      if i<j: arr[i], arr[j] = arr[j], arr[i]

  arr[high], arr[i] = arr[i], arr[high]
  return i


def quickSortIterative(arr, low, high):
  stack = [(low, high)]

  # Process stack until empty
  while stack:
    low, high = stack.pop()
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Push left and right sub-arrays to stack
        stack.append((low, pi - 1))
        stack.append((pi + 1, high))
  
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  