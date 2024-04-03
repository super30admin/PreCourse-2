# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode: I ran this code in VS Code editor in my local machine
# Any problem you faced while coding this: No


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  
    pivot = arr[h]

    # Set a pointer 1 position before the beginning of array
    i = l - 1

    for j in range (l, h):
        if arr[j] < pivot:
            i = i+1
            #Swap element of incremented i and j
            arr[i], arr[j] = arr[j], arr[i]
    # Finnaly swap element at pivot with i+1
    arr[i+1],arr[h] = arr[h], arr[i+1]

    # Returns starting position for next partition
    return i+1

def quickSortIterative(arr, l, h):
  # Initialize stack array with ther size of given array
  size = (h-1) + 1
  stack = [0]*size
  top = -1

  # Fill stack array with the l and h indexes of array
  top = top+1
  stack[top]=l
  top = top+1
  stack[top]=h

  while top>=0:
      h = stack[top]
      top = top -1
      l = stack[top]
      top = top-1

      pi = partition(arr,l,h)

      # If there are more than 1 elements on left side of partition index
      if (pi-1)>l:
          top = top+1
          stack[top]=l
          top = top+1
          stack[top]=pi-1
      # If there are more than 1 elements on right side of partition index
      if (pi+1)<h:
          top = top+1
          stack[top]=pi+1
          top = top+1
          stack[top]=h
        
    

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
print(arr[0:n])

