# Python program for implementation of Quicksort


# Time Complexity : O(nlog n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# We choose a pivot in the array(in this case, the last element) and then partition the array around the pivot.
# Then we recursively do the same for the left and right subarrays.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot =arr[h]
  i=l-1
  for j in range(l,h):
    if arr[j]<pivot:
      i+=1
      arr[j],arr[i]=arr[i],arr[j]
  arr[i+1],arr[h]=arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  size=h-l+1
  stack=[0]*size
  top=-1

  top+=1
  stack[top]=l
  top+=1
  stack[top]=h

  while top>=0:
    h=stack[top]
    top-=1
    l=stack[top]
    top-=1

    pivot=partition(arr,l,h)

    if pivot-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=pivot-1  

    if pivot+1<h:
      top+=1
      stack[top]=pivot+1
      top+=1
      stack[top]=h

arr = [4, 3, 5, 2, 1, 3, 2, 3]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print ("Sorted array is:")
for i in range(n):
    print ("% d" % arr[i]),

