# Python program for implementation of Quicksort Sort

# give you explanation for the approach

"""
This is recursive approach where I have taken the last element of the array as pivot .. we should check recursively whether the elements are less than pivot or not
If the current element (j) is less than pivot, it eans that it also less than the previous element (i) therefore, increment i and replave arr[i[ and arr[j]
finally, increment i and replace arr[i] and arr[high], there fore, the elements less than pivot will be less than pivot and greater than pivot will be rightside in each iteration
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i = i + 1
    temp = arr[high]
    arr[high] = arr[i]
    arr[i] = temp
    return i

    # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
# arr = [100, 67, 81, 80, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


