# Python program for implementation of Quicksort
#Time Complexity: O(n logn)
#Space Complexity: O(1)+O(n) stack space

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[l] #set the pivot
  i, j = l, h #set the i and j to the respective low and high pointers
  while i < j:
    while arr[i] <= pivot and i <= h-1: #Move i by 1 index to right if element at i is smaller than pivot and i less than high
      i+=1
    
    while arr[j] > pivot and j >= l+1: #Move j by 1 index to left if element at j is greater than pivot and j greater than low
      j-=1
    
    if i < j:
      arr[i], arr[j] = arr[j], arr[i] #Swap the elements at i and j only if i is less than j
  arr[l], arr[j] = arr[j], arr[l] #Swap the pivot element with element at index j
  return j # j is the partitioning point we return j



def quickSortIterative(arr, l, h):
  #write your code here
  stack = [] #Create a stack
  while l < h or len(stack) > 0: #Continue looping when both low is equal or greater than high and stack is empty
    if l < h: 
      pIndex = partition(arr, l, h) #Get partitioning index 
      stack.append([pIndex+1, h]) # First we solve the left part of a partition, but we will visit the right part later so we add the indices of the right subarray onto the stack
      h = pIndex - 1 # this will allow us to solve only the left part of the partition
    else:
      newLH= stack.pop() # pop out the indices of the right part
      l, h = newLH[0], newLH[1] #update the low and high to maintain the loop iteration 

arr = [4,3,5,2,1,3,2,3]
quickSortIterative(arr, 0, len(arr)-1)
print(f"After quickSortIterative {arr}")
    

