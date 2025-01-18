# Python program for implementation of Quicksort
#Time Complexity: Best Case: (nlogn) Worst Case:O(n^2)
#Space Complexity: O(n)
# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  # Choose the last element as pivot
    pivot = arr[h]
    i = l - 1 

    for j in range(l, h):
        # If current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at (i+1)
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
    stack = []
    stack.append((l, h))

    # Keep popping from the stack while it is not empty
    while stack:
        l, h = stack.pop()

        # Set pivot element at its correct position
        pivot = partition(arr, l, h)

        # If there are elements on the left of the pivot, push left subarray to the stack
        if pivot - 1 > l:
            stack.append((l, pivot - 1))

        # If there are elements on the right of the pivot, push right subarray to the stack
        if pivot + 1 < h:
            stack.append((pivot + 1, h))

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array is:")
    print(arr)

    quickSortIterative(arr, 0, len(arr) - 1)

    print("Sorted array is:")
    print(arr)
