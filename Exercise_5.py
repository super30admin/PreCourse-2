# Time Complexity:
# Average Case: O(n log n)
# Worst Case: O(n^2)

# Space Complexity:
# Average Case: O(log n)
# Worst Case: O(n)

# Did this code successfully run on LeetCode: Not directly applicable because LeetCode uses a different function format

# Any problem you faced while coding this: The main challenge was correctly storing and processing the left and right subarray boundaries using a stack instead of recursion

# Approach:
# 1. Store the initial low and high indices in a stack
# 2. Remove one range from the stack
# 3. Partition that range and place the pivot in its correct position
# 4. Add the left and right unsorted ranges to the stack
# 5. Continue until the stack is empty

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    stack = [(l, h)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

if __name__ == "__main__":
    test_cases = [
        [10, 7, 8, 9, 1, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 2, 4, 1, 2],
        [7],
        [],
    ]

    for arr in test_cases:
        expected = sorted(arr)
        quickSortIterative(arr, 0, len(arr) - 1)
        print("Sorted:", arr)
        print("Expected:", expected)
        print("Passed:", arr == expected)
        print()
