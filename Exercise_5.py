# Python program for implementation of Quicksort

# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
# Your code here along with comments explaining your approach :




# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l- 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    stack = [(l, h)]

    while stack:
        l, h = stack.pop()
        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            stack.append((l, pivot_index - 1))

        if pivot_index + 1 < h:
            stack.append((pivot_index + 1, h))



arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(arr[i])


