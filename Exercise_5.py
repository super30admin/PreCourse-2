# Python program for implementation of Quicksort
def swap(arr,i,idx):
    temp=arr[i]
    arr[i]=arr[idx]
    arr[idx]=temp
# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot=arr[h]
    i=l-1
    for idx in range(l,h):
        if(arr[idx]<pivot):
            i+=1
            swap(arr,i,idx)
    swap(arr,i+1,h)
    return i+1
  #write your code here

from queue import LifoQueue
def quickSortIterative(arr, l, h):
    stack=LifoQueue()
    stack.put(l)
    stack.put(h)
    while(stack.qsize()>0):
        high=stack.get()
        low=stack.get()
        p=partition(arr,low,high)
        if p-1>low:
            stack.put(low)
            stack.put(p-1)
        if p+1<high:
            stack.put(p+1)
            stack.put(high)
  #write your code here
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


