
 
def quickSortIterative(array,low,high):
    curr = -1
    curr+=1
    stackData = [0] * int(high - low + 1)
    stackData[curr] = low
    curr+=1
    stackData[curr] = high

    while curr >= 0:
        high = stackData[curr]
        curr-= 1
        low = stackData[curr]
        curr-= 1

        pv= partition( array, low, high )
        if pv+1 < high:
            curr+=1
            stackData[curr] = pv+ 1
            curr+=1
            stackData[curr] = high

        if pv-1 > low:
            curr+=1
            stackData[curr] = low
            curr+=1
            stackData[curr] = pv- 1

        

def partition(arr,low,high):
    i = ( low - 1 )
    x = arr[high]
 
    for j in range(low , high):
        if   arr[j] <= x:
 
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

arr = [1,10,2,4,15,18]
n = len(arr)
print("Before sorting Array:", arr)
quickSortIterative(arr, 0, n-1)
print ("After Sorted Array :", arr)