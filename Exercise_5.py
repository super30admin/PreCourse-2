"""
// Time Complexity :  O(nlogn), where n is the number of elements in the array
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : not on leetcode
// Any problem you faced while coding this : No
"""



# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  p = h #setting pivot to be the last element 
  i = l #setting i to start from the first element in arr
  
  for i in range(l, h): 
      
      if arr[i] < arr[p]: #if element smaller than the pivot element is found, we swap that element with low and increment low to point to the next position
          arr[i], arr[l] = arr[l], arr[i] #swap
          l = l+1
  arr[l], arr[p] = arr[p], arr[l] #after the loop terminates, low will be pointing to the correct position of the pivot element, hence we swap the values at low and p so that the pivot element is at its correct position
  return l #return the point where partition happens


def quickSortIterative(arr, l, h):
  #write your code here
  stack=[] #using stack to keep track of end points of all the lists created on partitioning 

  stack.append(l) #adding the initial values to the stack
  stack.append(h)

  while stack:
    high=stack.pop()
    low=stack.pop()

    p=partition(arr,low, high) #gets the pivot element

    if p-1>low: #if elements are present on the left side of the pivot, we add the end points from low to p-1 to the stack
      stack.append(low)
      stack.append(p-1)

    if p+1<high: #if elements are present on the right side of the pivot, we add the end points from p+1 to high to the stack
      stack.append(p+1)
      stack.append(high)


