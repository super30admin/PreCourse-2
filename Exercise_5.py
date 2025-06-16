# Python program for implementation of Quicksort

# Time: O(N log N) (avg case), O(N**2) (worst case)
# Space: O(log N) (avg case), O(N) (worst case)

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

# This function is same in both iterative and recursive
def partition(arr,low,high):
    #write your code here
    i = low-1
    pivot = arr[high]
    # Rearrange elements such that
    # if ele <= pivot, then place ele to the left of pivot
    # if ele > pivot, then place ele to the right of pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 # next index to store the small element A[j]
            swap(arr, i, j)

    i += 1 # next index to store the pivot
    # At this point, swap the pivot element with
    # A[i]. Here, i = position of the pivot element
    # in the sorted array. i splits the array into
    # two parts, left subarray and right subarray
    # elements of left subarray <= pivot
    # elements of right arr > pivot.
    # But elements in left arr and right arr are not sorted.
    swap(arr, i, high)
    return i


def quickSortIterative(arr, l, h):
  #write your code here
  N = len(arr)
  if N == 1:
        return arr[0]
  stack = []
  stack.append(l)
  stack.append(h)
  while stack:
        h = stack.pop()
        l = stack.pop()
        if l >= h:
            continue
        pivot_index = partition(arr, l, h)
         # right half of pivot
        if pivot_index < N-2:
          stack.append(pivot_index+1) # low
          stack.append(h) # high
        # left half of pivot
        if pivot_index > 0:
          stack.append(l) # low
          stack.append(pivot_index-1) # high

# Driver code to test above
# arr = [10, 7, 8, 9, 1, 5] # ans: [1, 5, 7, 8, 9, 10]
arr = [7, 6, 10, 5, 9, 2, 1, 15, 7] # ans: [1,2,5,6,7,7,9,10,15]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])