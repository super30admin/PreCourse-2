# Python program for implementation of Quicksort

def swap (arr, i, j):
    # swap function to swap elements at given indices
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

# This function is same in both iterative and recursive
def partition(arr, low, high):
    # O(n) time complexity | O(1) space complexity
    # write your code here
    count = 0  # count all elements lower than element at low index
    for i in range(low + 1, high + 1):
        if arr[i] < arr[low]:
            count += 1
    swap(arr, low, low + count)

    pivot = low + count

    while (low < pivot and high > pivot):  # push all lower elements to left and all higher elements to right
        if (arr[low] >= arr[pivot]):
            if (arr[high] < arr[pivot]):
                swap(arr, low, high)
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1

    return pivot  # return the pivot index


def quickSortIterative(arr, l, h):
  #write your code here
  # O(n.logn) Time Complexity | O(logn) Space Complexity
  # Didn't find it to be a better algorithm compared to recursive solution this time !!!

    stack = [l, h]              # initialize with low and high index values
    while (len(stack) != 0):
        high = stack.pop()      # pop the top two indices to perform partition in this range
        low = stack.pop()
        pivot = partition(arr, low, high)   # partition same as in recursion
        if (pivot - 1 > low):               # push low index to pivot-1 index if the range of indices is more than 1.
            stack.append(low)
            stack.append(pivot - 1)
        if (pivot + 1 < high):              # push pivot+1 index to high index if the range of indices is more than 1.
            stack.append(pivot + 1)
            stack.append(high)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5, 11]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),


