# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  pivot_index = l
  pivot_element = arr[pivot_index]
  while l<h:
    while l<h and arr[l] <= pivot_element:
      l += 1
    
    while arr[h] > pivot_element:
      h -= 1

    if l < h:
      arr[l], arr[h] = arr[h], arr[l]
  
  arr[pivot_index], arr[h] = arr[h], arr[pivot_index]
  return h

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.extend([l,h])

  while stack:
    high = stack.pop()
    low = stack.pop()

    if low < high:
      pivot_index = partition(arr, low, high)
      stack.extend([low,pivot_index-1])
      stack.extend([pivot_index+1, high])

# Driver code to test above 
# arr = [10, 7, 8, 9, 1, 5] 
arr = [9,5,3,2,4,21,4,7,4,2,5,7]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
