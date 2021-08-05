# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

def partition(arr, l, h):
    #write your code here
    pivot = arr[h]
    i = l
    for j in range(l,h):
        if arr[j] <= pivot:
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
    arr[i],arr[h] = arr[h], arr[i]
    return i

def quickSortIterative(arr, l, h):
    stack = []
    stack.append(l)
    stack.append(h)
    while len(stack):
        h,l = stack.pop(), stack.pop()
        if h<l: # when high gets lower than "high", we continue and look at next stack values
            continue
        p = partition(arr, l, h)
        stack.append(l)
        stack.append(p-1)
        stack.append(p+1)
        stack.append(h)
    return arr

print(quickSortIterative([4, 3, 5, 2, 1, 3, 2, 3], 0, 7))