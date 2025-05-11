# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = l
  left = l + 1
  right = h

  while left <=  right:
    if arr[left] >= arr[pivot] and arr[right] < arr[pivot]:
      arr[left], arr[right] = arr[right], arr[left]
    
    if arr[left] < arr[pivot]:
      left +=1
    if arr[right] >= arr[pivot]:
      right -=1
    
  arr[pivot],arr[right] = arr[right],arr[pivot]
  return pivot


def quickSortIterative(arr, l, h):
  #write your code here

  stack = [(l,h)]

  while stack:
    l,h = stack.pop()
    if l < h:
      p = partition(arr,l,h)
      stack.append((l,p-1))
      stack.append((p+1,h))
  
  return



arr = [3, 7,15, 16, 8, 3, 1, 15, 9, 3, 2]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 

