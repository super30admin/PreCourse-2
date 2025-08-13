# Python program for implementation of Quicksort
"""
Instead of using the call stack (recursion), we simulate it with our own stack. If we don’t use a stack and don’t use recursion, then you can’t do Quick Sort the classic way — because Quick Sort is fundamentally a divide and conquer algorithm that needs to remember the "left" and "right" subarrays for future sorting. You need some kind of memory structure to keep track of the subarray ranges.

Time Complexity: O(n2) in worst case, O(nlogn) average
In a typical run, the pivot splits the array into two roughly equal halves. So you do 
n (comparisons in partition)
+ n/2 + n/4 + ... + 1 = O(n log n). That’s a well-balanced divide-and-conquer.

Picking first or last element as pivot or the array is already sorted or reverse sorted gives a terrible split: one element vs the rest. So it does
(n - 1) + (n - 2) + ... + 1 = O(n2)

Space Complexity: O(n) in worst case, O(logn) average
Your explicit stack stores pairs of indices (l, h) that still need sorting. At any moment it can never hold more “live” sub-ranges than the height of the recursion tree. Height of that tree depends on pivot quality.
Balanced (random / median / middle)	≈ log₂ =	O(log n)
Degenerate (first/last pivot on sorted or reverse-sorted data) = n =	O(n)

A balanced pivot splits the array roughly in half each level → tree depth ≈ log n. A bad pivot keeps producing a 1 vs (n-1) split → depth n. So typical/average cases are O(log n); only the nightmare pivot pattern inflates it to O(n).
"""

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h] #pivot is last element
  i = l - 1
  
  for j in range(l, h): # pivot is at the end --> don't include it in the loop
    if arr[j] <= pivot:
      i += 1 # keep track of location to swap the elements
      arr[i], arr[j] = arr[j], arr[i]
     
  arr[i+1], arr[h] = arr[h], arr[i+1] # put pivot at its location
  return i+1 # return the index of the pivot


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [] # Stack for storing start and end indices
  stack.append((l, h)) # pushing a tuple to mimic a recursion stack
  
  while stack:
    l, h = stack.pop()
    if l < h: # if l == h, it is only one element and it is already sorted.
      pivot = partition(arr, l, h)
      
      if pivot + 1 < h: # RHS sort
        stack.append((pivot + 1, h))
      if l < pivot - 1: # LHS sort
        stack.append((l, pivot - 1)) 
  return arr


arr = [8, 4, 1, 56, 3, -44, 23, 5]
sorted_arr = quickSortIterative(arr, 0, len(arr) - 1)
print(sorted_arr)