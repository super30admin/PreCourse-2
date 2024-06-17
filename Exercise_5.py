# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
    
  i = l - 1
 
  for j in range(l, h):
      if arr[j] <= pivot:
          i = i + 1
          arr[i], arr[j] = arr[j], arr[i]
  
  arr[i + 1], arr[h] = arr[h], arr[i + 1]
  
  return i + 1

def quickSortIterative(arr, l, h):
    stack = []
    
    stack.append(0)
    stack.append(len(arr) - 1)
    
    while stack:
        h = stack.pop()
        l = stack.pop()
        
        pivot = partition(arr, l, h)
        
        if pivot - 1 > l:
            stack.append(l)
            stack.append(pivot - 1)
        
        if pivot + 1 < h:
            stack.append(pivot + 1)
            stack.append(h)

    return arr
    
  
print(quickSortIterative([5,4,3,2,1],0,5))


