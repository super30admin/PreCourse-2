# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
   pivot = arr[h]
   i = l - 1
   for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
   arr[i+1], arr[h] = arr[h], arr[i+1]
   return i+1


def quickSortIterative(arr, l, h):
  if len(arr) <= 1:
        return arr
    
  stack = []
  stack.append((0, len(arr)-1))
    
  while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            
            # Push left subarray
            if pi - 1 > low:
                stack.append((low, pi - 1))
            
            # Push right subarray
            if pi + 1 < high:
                stack.append((pi + 1, high))
    
  return arr

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])