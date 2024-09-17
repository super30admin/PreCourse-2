# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  curr,last = l,l
  while curr<=h:
      if arr[curr] < arr[h] or curr == h:
          arr[curr],arr[last] = arr[last],arr[curr]
          last += 1
      curr += 1

  return last-1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l,h)]
  c = 0
  while stack:
      l,h = stack.pop()
      if l < h:
        newP = partition(arr,l,h)
        if newP >= l:
            stack.append((l,newP-1))
            stack.append((newP+1,h))



arr = [10, 7, 8, 9, 1, 5] 
arr = [1,2,3,4,5]
arr = [3,2,1]
arr = [10,8,9,7,12,13,14,15,1,2,3,4,5]
#arr = [1,2]
arr = [8, 7, 2, 1, 0, 9, 6]
n = len(arr) 
print(arr)
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
