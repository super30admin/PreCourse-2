
#Time Complexity : O(n log n) in avg case  andd O(n^2) in worst case.
#Space Complexity: O(log n)

def partition(arr, l, h):
    pivot = arr[h]  # Choosing the last element as the pivot
    i = l - 1  # Index of the smaller element

    for j in range(l, h):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[h] = arr[h], arr[i + 1]  # Swap pivot with the element at the correct position
    return i + 1  # Return the partitioning index


def quickSortIterative(arr, l, h):
    stack = [(l, h)]

    while stack:
        l, h = stack.pop()

        if l < h:
            pivot_index = partition(arr, l, h)

            # Push the subarray indices to the stack
            stack.append((l, pivot_index - 1))
            stack.append((pivot_index + 1, h))
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quickSortIterative(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

