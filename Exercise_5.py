# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# Time Complexity: 
# - O(N^2) worst case scenario (when input array is already sorted)
# - O(Nlog(N)) average case scenario
# Reason: For 'N' elements it runs on average 'height of tree' times (log(N)).
# Space Complexity: O(log(N))
def partition(arr,l,h):
    pivot = arr[l]
    while l < h:
        # Find first element greater than or equal to pivot
        while l < h and arr[l] < pivot:
            l += 1

        # Find first element smaller than pivot
        while l < h and arr[h] > pivot:
            h -= 1

        # We want to find a position to insert our pivot at.
        # The idea of partition is to ensure all elements before pivot are smaller than it,
        # elements after pivot are greater than it.
        # If 'l' crosses 'h', we already have achieved our "partition" as explained above,
        # hence no need to swap, otherwise swap
        if l < h:
            arr[l], arr[h] = arr[h], arr[l]

    # Swap the pivot and element at 'h' to place pivot element to it's correct position
    pivot, arr[h] = arr[h], pivot
    return h


def quickSortIterative(arr, l, h):
    stack = [0] * (h - l + 1)

    # initial push for high and low
    stack[0] = l
    stack[1] = h

    top = 1

    # While stack is not empty, pop
    while top > -1:
      h = stack[top]
      top -= 1

      l = stack[top]
      top -= 1

      pivot = partition(arr, l, h)

      # Push elements on left of pivot to stack, i.e.
      # Perform quicksort on left array (left of pivot)
      if pivot - 1 > l:
          top += 1
          stack[top] = l

          top += 1
          stack[top] = pivot - 1
      
      # Push elements on right of pivot to stack, i.e.
      # Perform quicksort on right array (right of pivot)
      if pivot + 1 < h:
          top += 1
          stack[top] = pivot + 1

          top += 1
          stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
