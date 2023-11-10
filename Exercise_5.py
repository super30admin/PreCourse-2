# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
    pivot=arr[h]
    i=l-1
    #write your code here
    for a in range(l,h):
        if arr[a]<=pivot:

            i=i+1
            arr[i],arr[a]=arr[a],arr[i]
    
    arr[i+1],arr[h]=arr[h],arr[i+1]

    return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  if l<h:
        new=partition(arr,l,h)

        quickSortIterative(arr,l,new-1)

        quickSortIterative(arr,new+1,h)
