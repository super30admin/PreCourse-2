# Python program for implementation of MergeSort
#

# Time: O(N log N)
# Space: O(N)
def merge_sorted_arr(left, right):
    M = len(left)
    N = len(right)
    A = []
    n_inversions = 0

    if M == 0:
        A.extend(right)
        return A, n_inversions
    if N == 0:
        A.extend(left)
        return A, n_inversions

    i, j = 0,0
    while i<=M-1 and j<=N-1:
        if left[i] <= right[j]:
            A.append(left[i])
            i = i + 1
        else:
            A.append(right[j])
            j = j + 1
            n_inversions += M - i
    if i == M:
        A.extend(right[j:])
    if j == N:
        A.extend(left[i:])

    return A, n_inversions

# Time: O(N log N), Space: O(N)
def merge_sort(arr, lo, hi):
    N = hi - lo + 1
    assert N != 0, "Empty array, invalid"
    if N == 1:
        return [arr[lo]]

    mid = int((lo + hi)/2)
    left_arr = merge_sort(arr, lo, mid)
    right_arr = merge_sort(arr, mid+1, hi)
    A, _ = merge_sorted_arr(left_arr, right_arr)
    return A

def mergeSort(arr):

  #write your code here
  arr1 = merge_sort(arr, 0, len(arr)-1)
  return arr1

# Code to print the list
def printList(arr):
    #write your code here
    print(arr)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    sorted_arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(sorted_arr)
