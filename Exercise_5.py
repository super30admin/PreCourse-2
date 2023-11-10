# Time Complexity : O(n log n) for average case
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : 
# Any problem you faced while coding this : no

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

# last element is selected as pivot. 
def partition(arr,low,high):
  
    pivot=arr[high]
    i=low-1
    #loop through all the elements to compare with the pivot
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            (arr[i], arr[j])= arr[j], arr[i]    
    arr[i+1], arr[high]=arr[high], arr[i+1]    
    return i+1


def quickSortIterative(arr, l, h):
  size=h-l+1
  stack = [0]*(size)
  top=-1
  
  top=top+1
  stack[top]=l
  top=top+1
  stack[top]=h

  while top>=0:
    h=stack[top]
    top=top-1
    l=stack[top]
    top=top-1

    p=partition(arr, l, h)

    if p-1>l:
      top=top+1
      stack[top]=l
      top=top+1
      stack[top]=p-1

    if p+1<h:
      top=top+1
      stack[top]=p+1
      top=top+1
      stack[top]=h

if __name__=='__main__':
  a=[1,9,7,8,5,3,2,4]
  quickSortIterative(a, 0, len(a)-1)
  print("Sorted array is:\n")
  print(a)

