# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  index = l
  for i in range(l, h, 1):
      if arr[i] < pivot:
          arr[index],arr[i]=arr[i],arr[index]
          index += 1
  arr[index],arr[h]=arr[h],arr[index]
  return index

def quickSortIterative(arr, l, h):
      #write your code here
      stack= []
      stack.append(l)
      stack.append(h)
      while stack:

          h = stack.pop()
          l = stack.pop()

          p = partition(arr, l, h)

          if p - 1 > l:
              stack.append(l)
              stack.append(p - 1)


          if p + 1 < h:
              stack.append(p+1)
              stack.append(h)

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("array Before sorting ", arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:", arr)


