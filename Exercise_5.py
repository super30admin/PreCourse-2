# Time Complexity -  Best Case: O(n log n)  - Even partition
                     # Worst Case: O(n^2)  - Same elements throughout

# Space Complexity -
#   O(log n) for the stack 
#   O(n) in worst case stack usage for unbalanced partitions 

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here

  pivot = arr[h]  # Last element as pivot
  i = l - 1       # Index for smaller element

  for j in range(l,h):
    if arr[j] < pivot: # Current element is smaller than pivot, swap
      i+=1
      arr[i], arr[j] = arr[j], arr[i]
    
  arr[i + 1] , arr[h] = arr[h] , arr[i+1] # Put pivot at the correct position
  return i + 1 # Return pivot index


def quickSortIterative(arr, l, h):
  #write your code here

  stack =[]

   # Push initial l and h to stack
  stack.append((l, h))

  while stack:
    l, h = stack.pop()

    if l < h:
      # Partition array and get pivot index
      p = partition(arr, l, h)

          
      if p - 1 > l:  # If elements on left of pivot, push left side to stack
        stack.append((l, p - 1))

            
      if p + 1 < h: # If elements on right of pivot, push right side to stack
        stack.append((p + 1, h))

if __name__=="__main__":
    # Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSortIterative(arr,0,n-1) 
    print ("Sorted array is:") 
    for i in range(n): 
        print ("%d" %arr[i]), 

