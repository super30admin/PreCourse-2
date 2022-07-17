# Python program for implementation of Quicksort

# Time Complexity : O(nlogn)
# Space Complexity : O(n)  

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = ( l - 1 )
  x = arr[h]

  for j in range(l, h):
      if   arr[j] <= x:
          # increment index of smaller element
          i = i + 1
          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):
  # buffer stack
    size = h - l + 1
    stack = [0] * (size)
    top = -1
 
    # push l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # pop stack
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at right position
        p = partition( arr, l, h )
 
        # push left side if there are elements on left side of pivot
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # push right side if there are elements on right side of pivot
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

if __name__ == '__main__': 
  array_ = [7, 2, 8, 5, 1, 6, 2, 9]
  n = len(array_)
  quickSortIterative(array_, 0, n-1)
  print ("Sorted array is:")
  for i in range(n):
      print ("% d" % array_[i])