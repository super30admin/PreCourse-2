# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  i = (l - 1)     
  pivot = arr[h] 
 
  for j in range(l, h):
      if arr[j] <= pivot:
         
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
 
      arr[i + 1], arr[h] = arr[h], arr[i + 1]
      return (i + 1)
  #write your code here


def quickSortIterative(arr, l, h):
   if l < h:

        pi = partition(arr, l, h)

        quickSortIterative(arr, l, pi-1)
        quickSortIterative(arr, pi + 1, h)
  #write your code here

