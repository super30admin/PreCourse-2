# Python program for implementation of Quicksort


# This function is same in both iterative and recursive
def partition(arr, l, h):
    # write your code here
    # set last element as pivot
    pivot = arr[h]
    index = l - 1

    for num in range(l, h):
        if arr[num] <= pivot:
            index += 1
            arr[num], arr[index] = arr[index], arr[num]

    arr[index + 1], arr[h] = arr[h], arr[index + 1]
    return index + 1


def quickSortIterative(arr, l, h):
    # write your code here
    st = []

    st.append((l, h))

    while st:
        l, h = st.pop()

        pi = partition(arr, l, h)

        if pi - 1 > l:
            st.append((l, pi - 1))

        if pi + 1 < h:
            st.append((pi + 1, h))


if __name__ == "__main__":
    my_list = [3, 6, 8, 10, 1, 2, 1]
    n = len(my_list)
    quickSortIterative(my_list, 0, n - 1)
    print("Sorted array:", my_list)
