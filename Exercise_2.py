# Python program for implementation of Quicksort Sort

# Time Complexity : O(nlogn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Ran this in VS Code ide
# Any problem you faced while coding this : No

# give you explanation for the approach
def partition(arr, low, high):
    pivot = high
    rp = pivot - 1
    lp = low
    # assert high > low, "incorrect high > low"

    while True:

        # move right until left side of the array is less than pivot element
        while arr[lp] < arr[pivot] and lp < high:
            lp = lp + 1

        # move left until right side of the array is greater than pivot element
        while arr[rp] > arr[pivot] and rp > 0:
            rp = rp - 1

        # if the two pointers crossed over each other then break
        if lp >= rp:
            break
        # else swap the elements
        else:
            arr[lp], arr[rp] = arr[rp], arr[lp]

    # move the pivot element to it's right location
    arr[lp], arr[pivot] = arr[pivot], arr[lp]

    return lp

    # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):

    # partition places the pivot element at its right position
    partition_index = partition(arr, low, high)

    # sort elements before pivot point
    if partition_index - 1 >= low:
        quickSort(arr, low, partition_index - 1)

    # sort elements after the pivot point
    if partition_index + 1 < high:
        quickSort(arr, partition_index + 1, high)

    return arr


# Driver code to test above
# arr = [80, 90, 70, 60, 50, 40, 30]
arr = [7, 4, 1, 2, 5, 7, 9]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
