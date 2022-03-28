# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

#-----------------------------------------------------
# Time Complexity : O(n*n)  ---> n is the number of elements in the array
# Space Complexity : O (n) ---> n is the number of elements in the array
#---------------------------------------------------
def partition(arr, l, h):
  #write your code here
    i = (l - 1)         # index of smaller element
    pivot = arr[h]     # pivot
 
    for j in range(l, h):
 
        # If current element is smaller
        # than or equal to pivot
        if arr[j] <= pivot:
         
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


def quickSortIterative(arr, l, h):
  
  # Create stack 
  size = h - l + 1
  stack = [0] * (size) 

  # initialize top of stack 
  top = -1


  top = top + 1
  stack[top] = l 
  top = top + 1
  stack[top] = h 


  while top >= 0: 
      h = stack[top] 
      top = top - 1
      l = stack[top] 
      top = top - 1
      p = partition( arr, l, h ) 

      if p-1 > l: 
          top = top + 1
          stack[top] = l 
          top = top + 1
          stack[top] = p - 1

      if p+1 < h: 
          top = top + 1
          stack[top] = p + 1
          top = top + 1
          stack[top] = h 

arr = [10, 7, 8, 9, 1, 5]
#     []
#     [5, 1, 7, 9, 8, 10]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 