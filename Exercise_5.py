# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
#time complexity: O(n log n)
#space complexity: O(log n)
def partition(arr, l, h):
  #write your code here
  pivot = arr[l]  # Choosing the pivot as the first element
  i = l + 1  
    
  for j in range(l + 1, h+ 1):
        
        if arr[j] <= pivot:
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            # Increment index of smaller element
            i += 1
    
    # Swap pivot with the last element smaller than or equal to it
  arr[l], arr[i - 1] = arr[i - 1], arr[l]
    #returning the partitioning array 
  return i - 1


def quickSortIterative(arr, l, h):
    
  #write your code here
  '''

  Uses a stack to keep track of subarrays to be partitioned.
  Continues partitioning subarrays until the stack is empty
  '''
  stack = [(l, h)]  # Initialize stack with the initial low and high indices

  while stack:
        l, h = stack.pop()  # Pop the top element from the stack
        if l < h:
            pi = partition(arr, l, h)  # Partition the array and get the partitioning index
            # Push subarrays to the stack for further partitioning
            stack.append((l, pi - 1))  # Left subarray
            stack.append((pi + 1, h))  # R


# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:", arr)
#did not solve on leetcode

