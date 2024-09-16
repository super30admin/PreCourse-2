# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def partition(arr, l, h):
    #write your code here
    greater_ind = l
    pivot = arr[h]
    for curr_ind in range(l, h):
        if arr[curr_ind] < pivot:
            arr[curr_ind], arr[greater_ind] = arr[greater_ind], arr[curr_ind]
            greater_ind += 1
    arr[greater_ind], arr[h] = arr[h], arr[greater_ind]
    return greater_ind

# TIME COMPLEXITY: O(n^2) - O(n) calls to partition which itself is O(n)
# SPACE COMPLEXITY: O(n) - due to space of list_start_end - that has the number of calls to quicksortIterative.
def quickSortIterative(arr, l, h):
    #write your code here
    list_start_end = [(l, h)]
    while list_start_end:
        curr_start, curr_end = list_start_end.pop()
        pivot = partition(arr, curr_start, curr_end)
        if curr_start < pivot - 1:
            list_start_end.append((curr_start, pivot - 1))
        if curr_end > pivot + 1:
            list_start_end.append((pivot + 1, curr_end))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
