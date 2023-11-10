"""
Time Complexity : O(n*log(n) )
Space Complexity : O(n)
"""

def partition(arr, low, high):

    pivot = arr[low]
    pivot_pos = low
    i = low + 1
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[pivot_pos], arr[j] = arr[j], arr[pivot_pos]
    return j



def QuickSort(arr, low, high):

    if low < high:
        pivot_pos = partition(arr, low, high)
        QuickSort(arr, low, pivot_pos - 1)
        QuickSort(arr, pivot_pos + 1, high)


arr = [11,7,8,3,1]
QuickSort(arr, 0, len(arr) - 1)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])
