# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):

    # write your code here
    # Assigning pivot, lowest and highest elements

    pivot = arr[low]
    lowest = low + 1
    highest = high

    while True:

        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot

        while lowest <= highest and arr[highest] >= pivot:
            highest = highest - 1

        # Opposite process of the one above

        while lowest <= highest and arr[lowest] <= pivot:
            lowest = lowest + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop

        if lowest <= highest:
            arr[lowest], arr[highest] = arr[highest], arr[lowest]
            # The loop continues

        else:
            # we exit out of the loop
            break

    arr[low], arr[highest] = arr[highest], arr[low]

    return highest


# Function to do Quick sort
def quickSort(arr, low, high):

    # write your code here
    if low >= high:
        return

    p = partition(arr, low, high)
    quickSort(arr, low, p - 1)
    quickSort(arr, p + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),