# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    pivot = arr[h]
    pIdx = l
    for i in range(l, h):
        if arr[i] <= pivot:
            arr[i], arr[pIdx] = arr[pIdx], arr[i]
            pIdx += 1
    arr[pIdx], arr[h] = arr[h], arr[pIdx]
    return pIdx

def quickSortIterative(arr, l, h):
    stack = [(l, h)]
    while stack:
        l, h = stack.pop(0)
        mid = partition(arr, l, h)

        if mid-1 > l:
            stack.append((l, mid-1))
        if mid+1 < h:
            stack.append((mid+1, h))
        print(stack)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
