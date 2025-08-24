# Python program for implementation of Quicksort
# // Time Complexity : 
# // Space Complexity : 
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l -1 
  for j in range(l,h):
      if arr[j] <= pivot:
          i+=1
          arr[i], arr[j] = arr[j] , arr[i] 
  arr[i+1], arr[h] = arr[h], arr[i+1] 

  return i+1 


def quickSortIterative(arr, l, h):
  #write your code here
  # quick sort can be donw in 2 ways recursive or iterative
  # iterative approach is 
  # parition method takes care of putting the pivot in the right place making the array before pivot less than pivot and after the pivot greater than pivot
  # same way, lets do the parition until left is less than right
  # use stack to keep track of the left and right pivots 
  stack = [(l,h)] # intially sent the whole array range left to right 
  
  while stack: 
     l,h = stack.pop() # pops the first index and the last index
     if l<h: 
        p = partition(arr,l,h) # we first get the pivot , and we know the left of the pivot are less than the pivot, right > pivot
        stack.append((l,p-1)) # next is to sort the left array so keep sorting the left array, we know the left arra is sorted once the low index is less than the high index
        stack.append(p+1,h) # same with right subarray, sort the subarray
        # finally when both the arrays are sorted there will be no more elements in the stack and the array is sorted 





