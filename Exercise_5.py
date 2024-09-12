# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    position = l

    for i in range(l, h):
        if arr[h] > arr[i]:
            arr[i], arr[position] = arr[position], arr[i]
            position += 1
    arr[position], arr[h] = arr[h], arr[position]

    return position


def quickSortIterative(arr, l, h):
    # write your code here
    length = 1 + h - l
    res = length * [0]
    front = -1

    # Insert starting values
    front = front + 1
    res[front] = l

    front = front + 1
    res[front] = h

    while 0 <= front:
        h = res[front]
        front = front - 1

        l = res[front]
        front = front - 1

        # Set pivot 
        pivot = partition(arr, l, h)

        # Handling elements stored on the left to the pivot
        if pivot - 1 > l:
            front = front + 1
            res[front] = l
            front = front + 1
            res[front] = pivot - 1

        # Handling elements stored on the right to the pivot
        if pivot + 1 < h:
            front = front + 1
            res[front] = pivot + 1
            front = front + 1
            res[front] = h


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" ")
