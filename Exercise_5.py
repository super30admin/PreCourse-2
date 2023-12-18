# Python program for implementation of Quicksort
#The time complexity of the given QuickSort implementation (both recursive and iterative versions) is O(n log n) 
#Space complexity of the iterative version of QuickSort is O(log n) 

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
  #write your code here
  stack = [(l, h)]

  while stack:
        l, h = stack.pop()
        if l < h:
            pi = partition(arr, l, h)
            if pi - 1 > l:
                stack.append((l, pi - 1))
            if pi + 1 < h:
                stack.append((pi + 1, h))


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    print("Input array", arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array", arr)