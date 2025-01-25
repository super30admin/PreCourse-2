# Python program for implementation of Quicksort Sort 
  
# tc O(n log n), sc O(log n), but in worst case tc O(n^2) and sc O(n).
# the worst case tc and sc can be reduced by selecting middle element as pivot.
def partition(start, end):
    import random
    random_idx = random.randint(start, end)
    arr[random_idx], arr[start] = arr[start], arr[random_idx]
    
    left, right = start + 1, end
    
    while left <= right:
        if arr[left] <= arr[start]:
            left += 1
        elif arr[right] > arr[start]:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    arr[start], arr[right] = arr[right], arr[start]
    return right
            
    
def quickSort(arr, start, end):
    if start >= end:
        return
    pivot_idx = partition(start, end)
    quick(start, pivot_idx - 1)
    quick(pivot_idx + 1, end)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
