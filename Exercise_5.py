# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
## Space Complexity = O(n)
## Time Complexity = O(n)
def partition(arr, low, high):

  #write your code here
  # write your code here
  pivot = high
  i = -1

  for j in range(0, pivot):
      if arr[j] > arr[pivot]:
          continue
      else:
          i += 1

          arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

  return i + 1

def quickSortIterative(arr, low, high):
    print()
    stack = []
    # if low < high:
    #     p = partition(arr, low, high)
    #     print(arr, low, high)
    #     quickSort(arr, low, p - 1)
    #     quickSort(arr, p+1, high)

    stack.append((low,high))

    while stack:
        s, e = stack.pop()
        p = partition(arr, s, e)
        if p -1 > s:
            stack.append((s, p -1))
        if p+1 < e:
            stack.append((p+1,e))
  #write your code here

# Driver code to test above
arr = [10,2, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

