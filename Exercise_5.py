# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot=arr[l]
    i=l+1
    j=h
    while i<j:
        while arr[i]<= pivot and i<h-1:
            i +=1
        while arr[j]>pivot and j>l+1:
            j -=1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]  
    arr[l],arr[i]=arr[i],arr[l]
    return j        
  #write your code here


def quickSortIterative(arr, l, h):
  #write your code here
  # Need some help on how we will be using stack

