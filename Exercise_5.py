"""
Time Complexity : O(n^2)
Space Complexity : O(n)
"""
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    piv = arr[h]
    i = l - 1 
    
    for j in range(l, h):
        if arr[j] < piv:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[h], arr[i+1] = arr[i+1], arr[h]
    return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  top = -1
  size = h - l + 1
  stack = [0] * size
  
  top += 1 
  stack[top] = l
  top += 1 
  stack[top] = h
  
  while top >= 0:
      
      h = stack[top]
      top -= 1 
      l = stack[top]
      top -= 1
      
      piv = partition(arr, l, h)
      
      if piv - 1 > l:
          top += 1 
          stack[top] = l
          top += 1 
          stack[top] = piv - 1
          
      if piv + 1 < h:
          top += 1
          stack[top] = piv + 1
          top += 1 
          stack[top] = h
        
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end = " "), 
  
 