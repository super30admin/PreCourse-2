import numpy.random as random
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    ptr=l
    pivot=h
    for i in range(l,h):
        if arr[i]<arr[pivot]:
            arr[i], arr[ptr] = arr[ptr],arr[i] # swap
            ptr += 1
    arr[ptr] , arr[pivot] = arr[pivot], arr[ptr]
    return ptr

def quickSortIterative(arr, l, h):
  #write your code here
    stack=[l,h]
    while True:
        print(stack)
        if len(stack) == 0:
            break
        if (stack[-1]-stack[-2]) > 1:
            print(arr)
            p=partition(arr,stack[-2],stack[-1])
            # pop last two and insert l, p-1, p+1,h
            h=stack.pop(-1)
            l=stack.pop(-1)
            stack.append(l)
            stack.append(p-1)
            stack.append(p+1)
            stack.append(h)
        else:
            stack.pop(-1)
            stack.pop(-1)

arr = [1,1,4,4,6,21,5,7, 8,21, 9, 1,6,5,56,32,21,86,88]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])




