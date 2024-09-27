# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    #write your code here
    pivot = high
    i = low - 1
    for j in range(low, high):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def quickSortIterative(arr, l, h):
    #write your code here
    
    p = partition(arr, l, h)

    stack = []
    stack.append(0)
    stack.append(p-1)
    stack.append(p+1)
    stack.append(h)
    while len(stack):
        h = stack.pop()
        l = stack.pop()
        #print(h,l)
        if h > l:
            p = partition(arr, l, h)
            if p - 1 > l:
                stack.append(l)
                stack.append(p - 1)
            if p + 1 < h:
                stack.append(p + 1)
                stack.append(h)

arr = [12, 11, 13, 5, 6, 7, 1]  
quickSortIterative(arr, 0, len(arr)- 1)
print(arr)





