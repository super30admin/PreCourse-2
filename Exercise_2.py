"""
LeetCode: NA
TC/SC - see below
Challenge - logic  was very sensitive and needed a lot of debugging to fix it
"""

# Python program for implementation of Quicksort Sort

# give you explanation for the approach
# TC - O(N), SC- O(1)
def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        # find element to the right of pivot that is greater than pivot
        while i < high and arr[i] <= pivot:
            i += 1
        # find element to the left of pivot that is smaller than pivot
        while j > low and arr[j] > pivot:
            j -= 1
        # swap smaller with greater
        if i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    # put pivot in appropriate position making sure all elements smaller are in left and vice versa- swap j and low
    tmp = arr[j]
    arr[j] = arr[low]
    arr[low] = tmp

    # return new pivot position
    return j


# Function to do Quick sort
# TC- O(N^2) - worse case when pivot is on extreme, O(NlogN) if pivot is middle
# (equal list is divided making logN branches)
# SC - O(1), not counting recursion space
def quickSort(arr, low, high):
    if low < high:
        partitionPosition = partition(arr, low, high)
        quickSort(arr, low, partitionPosition - 1)
        quickSort(arr, partitionPosition + 1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
# arr = [2, 4, 6, 8, 9]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

'''
Scrachpad-
10 7 8 9 1 5
p
l          h  
*find l greater than p and r less than p*
      l      h *swap them if l < h*
'''
