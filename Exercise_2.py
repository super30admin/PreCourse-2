# // Time Complexity : O(nLogn) worst case O(n^2)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Had to revise some concepts of quicksort from CLRS and revisit basics.


# // Your code here along with comments explaining your approach

# give you explanation for the approach
def partition(arr, low, high):

    # Initializing pivot's index to low
    pivot_index = low
    pivot = arr[pivot_index]

    # This loop runs till low pointer is greater than
    # high pointer after that we'll swap the
    # pivot with element on high pointer
    while low < high:

        # Increment low pointer till it finds an
        # element greater than  pivot
        while low < len(arr) and arr[low] <= pivot:
            low += 1

        # Decrement the high pointer till it finds an
        # element less than pivot
        while arr[high] > pivot:
            high -= 1
        if(low < high):
            arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]

    # Returning high pointer
    return high


# Function to do Quick sort
def quickSort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)
        quickSort(arr,low, p - 1)
        quickSort(arr,p + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
