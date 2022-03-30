def partition(arr, low, high):
  #get last element from the arr and chose as pivot
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        #curent number being examined is less than pivot?
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    #swap the pivot
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #index of pivot after swap
    return i+1

def quickSortIterative(arr, low, high):
  #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # sorted array
        p = partition(arr, low, high )
        # push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),   