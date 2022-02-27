# Python program for implementation of Quicksort

'''
// Time Complexity : BEST WORST AVG O( N Log(N))
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :  Time limit exceeded , other cases succeeded though
// Any problem you faced while coding this : Tricky to convert recursion to iteration


// Your code here along with comments explaining your approach

'''
'''
This sort has following two portions ,
  1. Took first element as pivot , 
  iterate remaining with two pointer one from left and other from right use partition helper function this retruns right which is partition point
  2. Stack is used to call partition until all subarrays are called for sorting

- Partition
  1. When left is greter than pivot and right is less than pivot left and right are swapped
      When left is smaller than or equal to pivot increment left
      When right is greate or equal to pivot decrement right
  2. Swap pivot and right 

'''
# This function is same in both iterative and recursive
def partition(arr,start,end):
    p=start
    left=start+1
    right=end

    while right>=left:
        if arr[left]>arr[p] and arr[right]<arr[p]:
            arr[left],arr[right]=arr[right],arr[left]
        if arr[left]<=arr[p]:
            left+=1
        if arr[right]>=arr[p]:
            right-=1
    
    arr[p],arr[right]=arr[right],arr[p]
    return right


def quickSortIterative(arr, low, high):
  stack = []
  stack.append(low)
  stack.append(high)
  # print("Before",temp)
  while stack:  #while len(stack) is not 0:
    high=stack.pop()
    low= stack.pop()
    # print("In loop",temp, low,high)
    partition_idx = partition(arr,low,high)
    # print('Partition',pi,arr)
    if low < partition_idx -1:
        stack.append(low)
        stack.append(partition_idx -1)

    if partition_idx +1 < high:
        stack.append(partition_idx+1)
        stack.append(high)
  


  
# Driver code to test above 
# arr = [10, 7, 8, 9, 1, 5] 
arr=[-4,0,7,4,9,-5,-1,0,-7,-1]
print(arr)
quickSortIterative(arr,0,len(arr)-1)
print(arr)
  
 
