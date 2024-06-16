# Python program for implementation of Quicksort
#Time complexity is O(n^2)
#Space complexity is O(n)
# This function is same in both iterative and recursive


def partition(arr, low, high):
    pivot = arr[low]
    i = low +1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

    
def quickSortIterative(arr):
  #write your code here
      size = len(arr)
      stack = []
    
    # Push initial values of low and high to stack
      stack.append((0, size -1))
    
    # Keep popping from stack while it is not empty
      while stack:
          # Pop high and low
          low, high = stack.pop()
          
          # Set pivot element at its correct position in sorted array
          p = partition(arr, low, high)
          
          # If there are elements on left side of pivot, then push left side to stack
          if p - 1 >= low:
              stack.append((low, p - 1))
          
          # If there are elements on right side of pivot, then push right side to stack
          if p + 1 <= high:
              stack.append((p + 1, high))
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]  
quickSortIterative(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 
  