# Time: O(n log n) average, O(n^2) worst; Space: O(n) explicit range stack

def partition(arr, l, h):
    """Partition arr[l:h + 1] around its last element and return its index."""
    pivot = arr[h]
    boundary = l - 1
    for current in range(l, h):
        if arr[current] <= pivot:
            boundary += 1
            arr[boundary], arr[current] = arr[current], arr[boundary]
    arr[boundary + 1], arr[h] = arr[h], arr[boundary + 1]
    return boundary + 1


def quickSortIterative(arr, l, h):
    """Sort in place while storing pending ranges instead of using recursion."""
    if l >= h:
        return

    ranges = [(l, h)]
    while ranges:
        low, high = ranges.pop()
        pivot_index = partition(arr, low, high)
        # Only nontrivial ranges need processing.
        if low < pivot_index - 1:
            ranges.append((low, pivot_index - 1))
        if pivot_index + 1 < high:
            ranges.append((pivot_index + 1, high))


if __name__ == "__main__":
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    quickSortIterative(arr, 0, len(arr) - 1)
    print(*arr)
