# Time Complexity :O(N^2) for the worst case 
# Space Complexity : O(N) for the stack for worst case, O(logN) for the average case
# Did this code successfully run on Leetcode : I tried in VS code 
# Any problem you faced while coding this :Yes, was not sure how to do the iterative part like was not sure that stack was needed to be used

def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l,h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
  stack = []
  stack.append((l, h))
  while stack:
     l,h = stack.pop()
     if l < h:
        part = partition(arr, l, h)
        stack.append((l, part-1))
        stack.append((part + 1 , h))
        
arr = [10, 7, 8, 9, 1, 5, 1, 9]
quickSortIterative(arr, 0, len(arr) - 1)
print(arr)