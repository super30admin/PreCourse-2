'''
Python program for implementation of Quicksort

This function is same in both iterative and recursive

Time Complexity = O(n)
Space Complexity = O(1)
'''
def partition(arr, l, h):
  #write your code here
    i = l - 1
    pivot = arr[h]

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    # you should use a stack
    length_array = h - l + 1
    temp = [0] * length_array

    # start the top of the stack
    top = 0
    temp[top] = l
    top += 1
    temp[top] = h

    while top >= 0:
        # this is the basic structure to pop h and l
        h = temp[top]
        top -= 1
        l = temp[top]
        top -= 1

        # now you will need to pivot the element
        p = partition(arr, l , h)

        # instead of recursivley calling right and left, you will now push right or left of stack
        if p - 1 > l:
            top += 1
            temp[top] = l
            top += 1
            temp[top] = p - 1

        # now you will check the right side
        if p + 1 < h:
            top += 1
            temp[top] = p + 1
            top += 1
            temp[top] = h

arr = [1,2,3,4,5,6,7]
arr_2 = [4, 3, 5, 2, 1, 3, 2, 3]

quickSortIterative(arr_2, 0, len(arr_2)-1)

for i in range(0, len(arr_2)): print(arr_2[i])



