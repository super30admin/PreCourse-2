#Time complexity:  O(n^2)
# Space complexity: O(n)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h): # partition function for getting the  correct position of the element.
  #write your code here
  i = l-1
  pivot = arr[h]#setting the pivot element to the last position of the array.
  
  for j in range(l,h):
      if(arr[j]<=pivot):
          i = i+1
          temp = arr[i]
          arr[i] = arr[j]
          arr[j]= temp
  temp = arr[i+1]# Swapping the elements
  arr[i+1] = arr[h]
  arr[h]= temp
  return i+1

def quickSortIterative(arr, l, h):# Function to implement quick sort using iterative mechanism.
  #write your code here
  size = (h - l) + 1
  top = -1
  s = [0]* size# defining the stack 
  top = top + 1
  s[top]= l
  top = top + 1
  s[top] = h
  while top > -1:
    h = s[top]
    top = top - 1
    l = s[top]
    top = top - 1

    p = partition(arr,l,h) # calling the partition function.

    if p - 1 > l: # for left array.
      top = top + 1
      s[top] = l
      top = top + 1
      s[top] = p - 1

    if p + 1 < h: # for right array.
      top = top + 1
      s[top] = p + 1
      top = top + 1
      s[top] = h

arr = [2]
n = len(arr)
if len(arr) == 0:
  print("The array is empty")
elif len(arr) == 1:
  print("The sorted array contains only one element.", arr)
else:
  quickSortIterative(arr,0,n-1)
  print(" The Sorted array is ", arr) #printing the array.


