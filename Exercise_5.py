# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

# To iteratively perform quicksort instead of using the recursion stack we
# can create our own stack.

def partition(arr, low, high):
    pivot = arr[low]
    i,j = low + 1, low + 1
    while j <= high and j >= low + 1:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1
    
    arr[low], arr[i-1]= arr[i-1], arr[low]
    return i - 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l,h))
  while stack:
    low, high = stack.pop()
    if low <= high:
      pivot_index = partition(arr,low,high)
      stack.append((low,pivot_index-1))
      stack.append((pivot_index+1,high))
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
