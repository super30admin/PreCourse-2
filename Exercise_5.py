# Python program for implementation of Quicksort

# Time Complexity - O(nlogn) - Each iteration we divide the array by the pivot
# hence O(logn) and we traverse through the array to swap the elements
# lesser than pivot hence O(n).
# Space complexity - O(n) - Stack holding all the (l,h) combinations to be sent for partition.

# Taking element at last position(high) as pivot. Now traversing through the arr and
# swap all elements lesser than pivot to the pointer 'p'. Once traversing complete array
# is done, we swap pivot element with position 'p'. This makes all the elements before p
# lesser than pivot and all elements after p as greater than pivot. Now we need to sort the
# elements before and after pivot.
def partition(arr, l, h):
    pivot = arr[h]
    p = l
    for i in range(l, h):
        if arr[i] < pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    arr[p], arr[h] = arr[h], arr[p]
    return p

# Function to do Quick sort
# We keep dividing the array by the pivot and sorting the array before and after pivot.
# To store the divided array we make use of stack which holds the (start-(l), end-(h)) values
# of the array. For each pivot obtained we have 2 partitioned arrays possible. If for any
# combination l>=h then we skip it. We continue until stack is emptied.
def quickSortIterative(arr, l, h):
    stack = []
    stack.append((l,h))
    while stack:
        l,h = stack.pop()
        if l>=h:
            continue
        pivot = partition(arr, l, h)
        stack.append((l,pivot-1))
        stack.append((pivot+1,h))


# Driver code to test above
arr = [-100, -7, 8, 9, 10, 15]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),