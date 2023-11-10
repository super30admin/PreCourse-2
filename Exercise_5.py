# Python program for implementation of Quicksort
# time complexity = O(n)
# space complexity= O(n) 
# This function is same in both iterative and recursive
def partition(arr,low,high, pivot):
  while low<=high:
        while arr[low]<pivot:
            low+=1
        while arr[high]> pivot:
            high-=1
        if low<=high:
            arr[low], arr[high]=arr[high], arr[low]
            low+=1
            high-=1

  return low
  

def quickSortIterative(arr, low, high):
    stack = [0] * (len(arr))
    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        pivot= arr[int((high+low)/2)]
        p = partition( arr, low, high, pivot )
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
print(arr) 