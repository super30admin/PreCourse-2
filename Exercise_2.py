# Python program for implementation of Quicksort Sort


# give you explanation for the approach
def partition(arr, low, high):
    # write your code here
    # set last element as pivot
    pivot = arr[high]
    # index of the smaller element
    index = low - 1

    for num in range(low, high):
        # if current element is smaller or equal to pivot
        # then swap it with the smaller element
        if arr[num] <= pivot:
            index += 1
            arr[index], arr[num] = arr[num], arr[index]
    # swap the pivot element with the element at (index + 1)
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i])
