# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high, pivot):
    #write your code here
    
    while(low <= high):

        while(arr[low] < pivot):
            low += 1
        
        while(arr[high] > pivot):
            high -= 1

        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    return low

# in iterative approach we will maintain list(or rather stack) that keeps track of all
# start and end indices for the arr to use divide and conquer
def quickSortIterative(arr, l, h):
  #write your code here
  stack = list()
  stack.append((l,h))
  while stack:
    l, h = stack.pop()
    pivot = arr[(l+h)//2]
    idx = partition(arr, l, h, pivot)
    if idx - 1 > l:
      stack.append((l, idx-1))
    if idx < h:
      stack.append((idx, h))
  

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5 ,1, 5, 77, 33, 11, 878, 123 ] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
