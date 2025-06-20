#time complexity = O(nlogn)avg
#space complexity  = O(logn)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]
  i = l - 1
  for j in range(l, h):
     if(arr[j] <= pivot):
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return (i+1)


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append(l)
  stack.append(h)

  while (len(stack) != 0):
    h = stack.pop()
    l = stack.pop()
    p = partition(arr, l , h)
    if(l < p - 1):#if therre is an elemt in left stack 
      stack.append(l)
      stack.append(p-1)
    if(p+1 < h):
      stack.append(p+1)
      stack.append(h)
    
  

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
