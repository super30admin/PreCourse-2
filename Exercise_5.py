# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
    pivot= arr[h]  #pivot as the last element
    i=l-1
    for  j in range(l,h):
      if arr[j]<pivot:
        i+=1
        arr[i], arr[j]=arr[j],arr[i] #Swap the element if smaller one found

    arr[i+1] , arr[h] = arr[h], arr[i+1]
    return i+1  #index of the pivot

def quickSortIterative(arr, l, h):
  #write your code here
  stack =[(0,len(arr)-1)]
  while stack:
    l, h= stack.pop()

    if l<h:
      p=partition(arr,l,h)
      stack.append((l,p-1)) #push left subarray
      stack.append((p,h)) #push right subarray



arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n - 1)
print("Sorted array:", arr)
