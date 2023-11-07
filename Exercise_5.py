# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i=l-1
    
  for j in range(l,h):
    if arr[j]<=pivot:
      i+=1
      arr[j],arr[i]=arr[i],arr[j]
        
  arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):

    if len(arr) <= 1:
        return arr
    
    stack = [(l,h)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
            else:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
quickSortIterative(arr,0,len(arr)-1)
print(arr)

  #write your code here

