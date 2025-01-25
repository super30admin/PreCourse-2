# Python program for implementation of Quicksort

def random_partition(arr, low, high):
    # Swapping arr[high] with any random element in the array and then partitioning around
    # pivot_element = arr[high].
    import random
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = low
    pivot_element = arr[high]

    for i in range(low, high):
        if arr[i] < pivot_element:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot += 1

    # Taking pivot_element to pivot position.
    arr[pivot], arr[high] = arr[high], arr[pivot]
    return pivot

def quick_sort(arr):
    n = len(arr)
    helper = [(0, n - 1)]

    while helper:
        low, high = helper.pop()

        pivot = random_partition(arr, low, high)

        if pivot - 1 > low:
            helper.append((low, pivot - 1))
        if pivot + 1 < high:
            helper.append((pivot + 1, high))

    return arr

