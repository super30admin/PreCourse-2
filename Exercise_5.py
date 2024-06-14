#Time Complexity : O(nlogn)
#Space Complexity : O(logn)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

#This function takes the last element of the array (arr[high]) as the pivot, places the pivot element at its correct position in sorted array, and places all smaller elements (smaller than pivot) to the left of the pivot and all greater elements to the right of the pivot.
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  pindex = l
  for k in range(l,h):
    if arr[k] <= pivot:
      arr[pindex],arr[k] = arr[k],arr[pindex]
      pindex += 1
    # Swap arr[pindex] and arr[high] to place the pivot in its correct position
  arr[pindex],arr[h] = arr[h],arr[pindex]
  return pindex

def quickSortIterative(arr, l, h):
  #write your code here
  # Initialize an auxiliary stack with initial low and high indices
    aux_stack = [(l,h)]
    # Iterate until the stack is empty
    while aux_stack:
        l,h = aux_stack.pop()
        # Partition the array and get the pivot index
        if l < h:
            piv_index = partition(arr,l,h)
        # Push subarray indices to the stack
            if piv_index - 1 > l:
                aux_stack.append((l,piv_index - 1))
            if piv_index + 1 < h:
                aux_stack.append((piv_index + 1, h))
arr = [10, 7, 8, 9, 2, 6]
quickSortIterative(arr,0,len(arr)-1)
print("Sorted array : ", arr)
    



