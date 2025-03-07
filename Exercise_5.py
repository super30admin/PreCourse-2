# Python program for implementation of Quicksort
#Time complexity:Best -> O(n logn) Worst -> O(n2)
#Space complexity:Best -> O(logn) Worst -> O(n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h] # choosing last elemrnt as pivot
  i = l - 1 # pointer for smaller elements
  for j in range(l,h): #traverse from low to high
      if arr[j] <= pivot: #if elements smaller or equal to pivot
          i += 1 #increment low pointer
          arr[i],arr[j] = arr[j],arr[i] #swapping lower element to the left
  arr[i+1],arr[h] = arr[h],arr[i+1] #swapping pivot element to the correct position
  return i+1 #returning partition index


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l,h))
  while stack:
     l,h = stack.pop()
     if l < h:
        pivotIndex = partition(arr,l,h)
        # Push left part onto stack if it has more than 1 element
        if pivotIndex - 1 > l:
            stack.append((l, pivotIndex - 1))
        
        # Push right part onto stack if it has more than 1 element
        if pivotIndex + 1 < h:
            stack.append((pivotIndex + 1, h))

arr = [10, 7, 8, 9, 1, 5] 
print("Before Sorting: ",arr)
n = len(arr)
quickSortIterative(arr,0,n-1) 
print("After Sorting: ",arr)