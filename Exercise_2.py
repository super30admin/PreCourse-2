# Python program for implementation of Quicksort Sort


# give you explanation for the approach

"""
Time Complexity :O(nLog(n))
"""


def partition(arr, low, high):

    # write your code here

    myP = arr[high]

    PIndex = low
    for i in range(low, high):
        if arr[i] <= myP:
            temp = arr[i]
            arr[i] = arr[PIndex]
            arr[PIndex] = temp
            PIndex += 1
    temp = arr[high]
    arr[high] = arr[PIndex]
    arr[PIndex] = temp

    return PIndex

# Function to do Quick sort


def quickSort(arr, low, high):

    # write your code here

    if low >= high:
        return
    PIndex = partition(arr, low, high)
    quickSort(arr, low, PIndex-1)
    quickSort(arr, PIndex+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
