"""
Time complexity : O(nlogn)
Space Complexity: O(n)

"""


def partition(arr,low,high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i+1])

    return i + 1


def quickSortIterative(arr, l, h): 
  
    size = h - l + 1
    stack = [0] * (size) 

    t = -1
    t = t + 1
    stack[t] = l 
    t = t + 1
    stack[t] = h 
  
    
    while t >= 0: 

        h = stack[t] 
        t = t - 1
        l = stack[t] 
        t = t - 1

         
        p = partition( arr, l, h ) 
  

        if p-1 > l: 
            t = t + 1
            stack[t] = l 
            t = t + 1
            stack[t] = p - 1
  

        if p + 1 < h: 
            t = t + 1
            stack[t] = p + 1
            t = t + 1
            stack[t] = h 


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
