# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while left <= right and arr[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right
  #write your code here


def quickSortIterative(arr, low, high):
    size = high - low + 1
    stack = [0] * size
    top = -1
    top +=1
    stack[top] = low
    top += 1
    stack[top] = high

    while top >=0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -=1
        p = partition(arr, low, high)

        if p-1 >low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = p-1

        if p+1 <high:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = high
  #write your code here

arr = [10,7,8,9,1,5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is :")
for i in range(n):
    print ("%d" %arr[i])
