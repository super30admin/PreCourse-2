def partition(arr, low, high): 
    i = ( low-1 )          
    pivot = arr[high]     
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )
  
def quickSort(arr,l,h): 
    size = h - l + 1
    stack = [0] * (size) 
  
    top = 0
    stack[top] = l 
    top = top + 1
    stack[top] = h 

    while top >= 0: 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
        partition_index = partition( arr, l, h ) 

        if partition_index-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = partition_index - 1
  
        if partition_index+1 < h: 
            top = top + 1
            stack[top] = partition_index + 1
            top = top + 1
            stack[top] = h 
    
  
# Driver Code 
arr = [100, 151, 5, 92, 2, 3, 88, 23, 10, 9, 44] 
n = len(arr) 
print("Array before sorting:") 
print(arr)
quickSort(arr, 0, n - 1) 
print("Array after sorting:")
print(arr)