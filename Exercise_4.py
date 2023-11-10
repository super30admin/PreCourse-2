# Time Complexity: O(NlogN), as we divide the element at each step and that would take logn and we
# visit the every node getting to n steps
# Space Complexity: O(N) as we are storing the result in a sorted array
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort
def merge(left,right):

  l = 0
  r = 0
  left_size = len(left)
  right_size = len(right)
  sorted_l = list()

  while((l < left_size) and (r < right_size)):
    if(left[l] <= right[r]):
        sorted_l.append(left[l])
        l+=1
    else:
        sorted_l.append(right[r])
        r+=1

  if (l < left_size):
      sorted_l += left[l:]
  elif(r < right_size):
      sorted_l += right[r:]

  return sorted_l

def mergeSort(arr, l, r):
  if (len(arr) <=1):
      return arr
  mid = len(arr)//2
  # left = arr[mid:]
  # right = arr[:mid]
  sleft = mergeSort(arr[:mid],0,mid-1)
  sright = mergeSort(arr[mid:],mid-1,r)
  return merge(sleft,sright)

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
      print(arr[i], end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
  arr = [12, 11, 13, 5, 6, 7]
  print ("Given array is", end="\n")
  printList(arr)
  # print(exit)
  sorted_array = mergeSort(arr, 0, len(arr)-1)
  print("Sorted array is: ", end="\n")
  printList(sorted_array)