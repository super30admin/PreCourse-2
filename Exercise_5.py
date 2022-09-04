# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
  pivot, i = arr[h], l - 1
  for j in range(l, h):
    if arr[j] <= pivot:
      i = i+1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i+1], arr[h]) = (arr[h], arr[i+1])
  return i+1

def quickSortIterative(arr, l, h):

  #write your code here
  if l < h:
    pi = partition(arr, l, h)
    quickSortIterative(arr, l, pi-1)
    quickSortIterative(arr, pi+1, h)  
     
    
    #write your code here
  
# Driver code to test above 
arr = [17, 6, 12, 19, 0, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
print (arr)
