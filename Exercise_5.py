def partition(arr,low,high):
    #write your code here
    #picking the last element as pivot
    j = low
    for i in range(low,high):
      if arr[i] <= arr[high]:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    size = high - low + 1
    stack = [0] * (size)
 
    # initialize stack
    top = -1
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # pop from stack while is not empty
    while top >= 0:
 
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 

        p = partition(arr, low, high)
 
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
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
