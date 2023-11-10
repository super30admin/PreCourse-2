# Python program for implementation of Quicksort
# I wasn't able to come up with this solution on my own. Had to refer other resources.
# Time complexity = O(nlogn) best case and average case  --> O(n^2) in the worst case
# Space complexity = O(n) for the stack that we're using to store the elements

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    i = l - 1
    x = arr[h]
    for j in range(l, h):
        if arr[j] <= x:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def quickSortIterative(arr, l, h):
    #write your code here
    size = h - l +1
    stack = [0] * (size)

    top = -1
    top+=1
    stack[top] = l
    top +=1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top-=1
        l = stack[top]
        top-=1

        p = partition(arr,l, h)
        if p - 1> l:

            top+=1
            stack[top] =l
            top+=1
            stack[top] = p-1
        if p+1 < h:
            top +=1
            stack[top] = p+1
            top +=1
            stack[top] = h


arr = [23,12,34,33,56]
n = len(arr)
quickSortIterative(arr, 0 , n-1)
for ele in arr:
    print(ele, end = " ")