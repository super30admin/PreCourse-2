def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back into arr in-place
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Compare elements from left_half and right_half and merge into arr
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_half or right_half if there are any
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

merge_sort(arr)
print("Sorted array:", arr)
