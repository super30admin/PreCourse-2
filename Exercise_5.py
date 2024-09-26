# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    #we always pick the last element as pivot
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[high] = arr[high],arr[i]
    return i


def quickSortIterative(arr, low, high):
    # Create an auxiliary stack 
    stack = []
    stack.append((low, high))

    while stack:
        low, high = stack.pop()
        pindex = partition(arr, low, high)
        
        if pindex - 1 > low:
            stack.append((low, pindex - 1))
        if pindex + 1 < high:
            stack.append((pindex + 1, high))


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])