# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    start = l - 1
    pivot = arr[h]

    for i in range(l,h):

        if arr[i] <= pivot:

            start += 1

            #swap
            temp = arr[start]
            arr[start]= arr[i]
            arr[i] = temp

    swap = arr[start + 1]
    arr[start + 1] = arr[h]
    arr[h] = swap

    return start + 1
  #write your code here

#need to implement using stack to keep order of elements
def quickSortIterative(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)


    head = -1


    head = head + 1
    stack[head] = l
    head = head + 1
    stack[head] = h


    while head >= 0:


        h = stack[head]
        head = head - 1
        l = stack[head]
        head = head - 1


        pivot = partition( arr, l, h )


        if pivot-1 > l:
            head = head + 1
            stack[head] = l
            head = head + 1
            stack[head] = pivot - 1


        if pivot+1 < h:
            head = head + 1
            stack[head] = pivot + 1
            head = head + 1
            stack[head] = h
  #write your code here

