# Time Complexity : O()
# Space Complexity : O()
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : I am not sure how iterative method works, so I am unable to do it. 
#I want to spend more time with it so I am submitting other problems and will work on this.

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[high]
  i = low-1
  for j in range(low,high):
    if arr[j] <= pivot:
      i = i+1
      arr[i],arr[j] = arr[j],arr[i]        
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )   


def quickSortIterative(arr, l, h):
  #write your code here

