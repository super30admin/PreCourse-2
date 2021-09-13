# Python program for implementation of Quicksort
# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot_index = low
  pivot = arr[pivot_index]
  while low < high:
      while low < len(arr) and arr[low] <= pivot:
          low+=1
      while arr[high] > pivot:
          high-=1
      if low < high:
          swap(low, high, arr)
  swap(pivot_index, high, arr)
  return high

def swap(i, j, arr):
    if i!=j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

def quickSortIterative(arr, l, h):
  #write your code here
  stack=[]
  stack.append(l)
  stack.append(h)
  while len(stack)!=0:
      end=stack.pop()
      start=stack.pop()
      if end-start<2:
          continue
      pi=partition(arr,start,end)
      stack.append(pi+1)
      stack.append(end)
      stack.append(start)
      stack.append(pi-1)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

