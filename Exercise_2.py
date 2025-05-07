# Python program for implementation of Quicksort Sort
# Time complexity : o(nlogn)
# space complexity o(n)

# give you explanation for the approach
def partition(arr, low, high):
    left, pivot = low, arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            temp = arr[i]
            arr[i] = arr[left]
            arr[left] = temp
            left+=1
    arr[high] = arr[left]
    arr[left] = pivot
    return left
        

def quickSort(arr, low, high):
    if high - low + 1 <= 1:
        return arr
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
