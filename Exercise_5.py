# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):


    p= h # Pivot
    small= l
    for i in range(l, h+1):
       if arr[i] < arr[p]:
            arr[i], arr[small]= arr[small], arr[i]
            small+=1
    # Swap small and pivot.
    arr[small], arr[p]= arr[p], arr[small]
    return small


def quickSortIterative(arr, l, h):
  #write your code here
  stack = []

  stack.append(l)
  stack.append(h)

  while stack : 
    h = stack.pop()
    l = stack.pop()
    p = partition(arr, l, h)

    if l < p-1 : 
      stack.append(l)
      stack.append(p-1) 

    if h > p+1 : 
      stack.append(p+1)
      stack.append(h)




# Driver code to test above 
arr = [4, 3, 5, 2, 1, 3, 2, 3] 
n = len(arr) - 1
quickSortIterative(arr, 0, n) 
print ("Sorted array is:") 
for i in range(n+1): 
    print ("%d" %arr[i])