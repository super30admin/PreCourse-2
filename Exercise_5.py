# Time complexity: O(nlog(n)) ; n = no. of elements
# Space complexity: O(n) 

# Python program for implementation of Quicksort

def partition(arr, lo, hi):
  #write your code here
    i = lo - 1
    p = arr[hi]
    for j in range(lo, hi):
        if arr[j] <= p:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def iterativeQSort(arr, lo, hi):
  #write your code here
    stack = [0] * (hi - lo + 1)
    top = -1
    top = top + 1
    stack[top] = lo
    top = top + 1
    stack[top] = hi

    while top >= 0:
        hi = stack[top]
        top = top - 1
        lo = stack[top]
        top = top - 1
        p = partition(arr, lo, hi)
        if p - 1 > lo:
            top = top + 1
            stack[top] = lo
            top = top + 1
            stack[top] = p - 1
        if p + 1 < hi:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = hi

arr = [10,1,2,6,4,8,0,12]
print("Before Quicksort: ", arr)
iterativeQSort(arr, 0, len(arr)-1)
print ("After Quicksort: ", arr)
