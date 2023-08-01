# Time Complexity : average and worst-case time complexity is O(n log n).
# Space Complexity : O(log n) on average and O(n) in the worst case due to the stack space used for simulating the iterative process. (In place sorting take O(1) space complexity)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h] #Selecting the last element of the array as the pivot element
  i = l-1 
  for j in range(l,h): #Traversing through all the elements
      if arr[j] <= pivot: #Comparing the elements with the pivot
          i += 1 #If the element is less than or equal to pivot, swap it with the element at i+1 index
          (arr[i], arr[j]) = (arr[j], arr[i])
    
  (arr[i+1], arr[h]) = (arr[h], arr[i+1])  #Swap the pivot element to its correct sorted position
  return i+1 #return the pivot index


def quickSortIterative(arr, l, h):
  stack = [(l,h)] #Create an auxiliary stack

  while stack:
    l,h = stack.pop()
    if l<h:
      pivot_index = partition(arr, l, h)
      #Push the sub-arrays to the stack for further sorting
      stack.append((l, pivot_index - 1))
      stack.append((pivot_index + 1, h))