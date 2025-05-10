# // Time Complexity : O(n log n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this :No



# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
      # Considering 1st elem as pivot
    pivot = arr[l]
    # Two pointers 
    pointer_1 = l + 1
    pointer_2 = h

    while True:
        # Stop pointer_1 at the first number greater than or equal pivot
        while pointer_1 <= h and arr[pointer_1] <= pivot:
            pointer_1 += 1
        # Stop pointer_2 at the number smaller than pivot
        while pointer_2 > l and arr[pointer_2] > pivot:
            pointer_2 -= 1
        # Stop the loop when pointer_2 crosses pointer_1
        if pointer_1 >= pointer_2:
            break
        # Swapping the elements at i,j
        arr[pointer_1], arr[pointer_2] = arr[pointer_2], arr[pointer_1]
    # Swapping such that pivot is placed correctly
    arr[l], arr[pointer_2] = arr[pointer_2], arr[l]
    return pointer_2

def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(0, len(arr) - 1)]

  while stack:
      l, h = stack.pop()
      if l < h:
          pi = partition(arr, l, h)
          stack.append((l, pi - 1))
          stack.append((pi + 1, h))


# arr = [10, 27, 80, 9, 11, 75, 56]
# n=len(arr) - 1
# quickSortIterative(arr,0,n)
# print("Sorted array:", arr)
