# Python program for implementation of Quicksort

# TODO:
#     Time Complexity = Big O(Nˆ2) worst case, Big O(NlogN) best case
#     Space Complexity = Big O(N)

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h]
    index = l
    for i in range(l,h):
        if arr[i] <= pivot:
            arr[i], arr[index]= arr[index], arr[i]
            index += 1
    arr[index], arr[h] = arr[h], arr[index]
    return index
  #write your code here


def quickSortIterative(arr, l, h):
  #write your code here
  stack, start, end = [], 0, len(arr)-1
  stack.append((start,end))

  while stack:
      start,end = stack.pop() # get sub list range
      p = partition(arr,start,end)

      if p-1>start: # push indices less than pivot point to stack
          stack.append((start,p-1))

      if p+1<end: # push indices greater than pivot point to stack
          stack.append((p+1,end))


if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),


