# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot=arr[h]
  start=l
  for end in range(l,h):
    if arr[end]<=pivot:
      arr[start],arr[end]=arr[end],arr[start]
      start+=1
  arr[start],arr[h]=arr[h],arr[start]
  return start


def quickSortIterative(arr, l, h):
  #write your code here
  callstack=[]
  callstack.append((l,h))
  while callstack:
    l,h=callstack.pop()
    if l<h:
      pivot = partition(arr,l,h)
      if pivot-1>l:
        callstack.append((l,pivot-1))
      if pivot+1<h:
        callstack.append((pivot+1,h))

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Before:", arr)

    quickSortIterative(arr, 0, len(arr) - 1)

    print("After: ", arr)


