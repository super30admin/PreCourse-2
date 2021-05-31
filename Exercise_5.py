# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = l - 1
  pivot = arr[h]  # Assign last element as pivot value and then compare it with the rest of the array elements

  for j in range(l, h):
      if(arr[j] <= pivot):
          i += 1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  return (i + 1)


def quickSortIterative(arr, l, h):
    n = h - l + 1
    stack = [0] * n #Auxilary Stack
    top = -1

    top = top +1   # Initial value push() to stack
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]   #Pop() high and Low
        top = top - 1
        l = stack[top]
        top = top - 1

        part = partition(arr, l, h)  # Setting Pivot Element

        #For Elements in the left of pivot
        if part-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = part - 1

        # For Elements in the right of pivot
        if part + 1 < h:
            top = top + 1
            stack[top] = part + 1
            top = top + 1
            stack[top] = h


arr = [5, 4, 6, 3, 2, 5, 4, 2,8]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),




