# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
# Time Complexity : O(nlogn)
# Space Complexity : O(1)
def partition(arr, l, h):
#write your code here
  low = l - 1
  high = arr[h]
  
  for i in range(l,h):
      if arr[i] <= high:
          low +=1
          
          arr[low], arr[i] = arr[i], arr[low]
          
  arr[low+1], arr[h] = arr[h], arr[low+1]
  
  return low+1

def quickSortIterative(arr, l, h):
#write your code here
  count = -1
  lenn = h - l + 1
  li = [0] * lenn
  count +=1
  li[count] = l
  count +=1
  li[count] = h

  while count >=0:
      h = li[count]
      count -=1
      l = li[count]
      count -=1
        
      par = partition(arr,l,h)
        
      if par-1 > l:
          count +=1
          li[count] =l
          count +=1
          li[count] = par-1
          
      
      if par+1 < h:
          count +=1
          li[count] = par+1
          count +=1
          li[count] = h

arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
print(arr)
      