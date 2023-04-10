# Python program for implementation of Quicksort
def swap (arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  count = 0  
  for i in range(low + 1, high + 1):
      if arr[i] < arr[low]:
          count += 1
  swap(arr, low, low + count)

  pivot = low + count

  while (low < pivot and high > pivot):  
      if (arr[low] >= arr[pivot]):
          if (arr[high] < arr[pivot]):
              swap(arr, low, high)
              low += 1
              high -= 1
          else:
              high -= 1
      else:
          low += 1

  return pivot  



def quickSortIterative(arr, l, h):
  #write your code here
  stack = [l, h]             
    while (len(stack) != 0):
      high = stack.pop()    
      low = stack.pop()
      pivot = partition(arr, low, high)   
      if (pivot - 1 > low):        
          stack.append(low)
          stack.append(pivot - 1)
      if (pivot + 1 < high):             
          stack.append(pivot + 1)
          stack.append(high)


arr = [10, 7, 8, 9, 1, 5, 11]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),