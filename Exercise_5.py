#Time Complexity: O(n^2) worst case
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSortIterative(arr,l,h):
  
    size = h - l + 1
    aux_array = [0] * (size)
  
    top = -1
  
    top = top + 1
    aux_array[top] = l
    top = top + 1
    aux_array[top] = h
  
    while top >= 0:
  
        h = aux_array[top]
        top = top - 1
        l = aux_array[top]
        top = top - 1
  
        p = partition( arr, l, h )
  
        if p-1 > l:
            top = top + 1
            aux_array[top] = l
            top = top + 1
            aux_array[top] = p - 1
  
        if p+1 < h:
            top = top + 1
            aux_array[top] = p + 1
            top = top + 1
            aux_array[top] = h


arr = [4, 3, 5, 2, 1, 3, 2, 3]
print(arr)
size=len(arr)
quickSortIterative(arr,0,size-1)
print(arr)



