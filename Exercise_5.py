# Python program for implementation of Quicksort
#time complexity O(N log N)
#space complexity O(log N) 

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
 size = h - l + 1
 stack = [0] * size
 top = -1

 top += 1
 stack[top] = l
 top += 1
 stack[top] = h

 while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot_index - 1

        if pivot_index + 1 < h:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = h


# Driver code
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n - 1):
        print(arr[i], end=" ")
    print(arr[n - 1])

