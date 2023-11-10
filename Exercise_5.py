# Quicksort Time Complexity, Best Case: O(nlog(n)), Worst Case: O(n^2)
# Quicksort Space Complexity: O(log(n)), worst case: O(n)
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  #initializing the pivot element 
  pivot=h
  h=h-1
  #all the elements smaller than pivot are moved on left and elements greater than pivot are moved onto right
  while l<h:
    if arr[l]<arr[pivot]:
      l+=1
    if arr[h]>arr[pivot]:
      h-=1
    else:
      #if element on the left is not smaller and element on the right is not greater than pivot swap them
      arr[l],arr[h]=arr[h],arr[l]
  if l>=h:
    arr[l],arr[pivot]=arr[pivot],arr[l]
  return l

def quickSortIterative(arr, l, h):
  #write your code here
  #initializing a stack with length similar to the array size
  stack=[0]*len(arr)
  #initializing top 
  top=-1
  # pushing low index of the array in the stack and incrementing top
  top+=1
  stack[top]=l
  #incrementing top and pushing the high index of the array into stack
  top+=1
  stack[top]=h

  #while there are elements in the stack
  while top>=0:
    #popping the stack to get the index values of high and low. Decrementing top after popping
    h=stack[top]
    top-=1
    l=stack[top]
    top-=1
    #getting the partition value
    partition_val=partition(arr,l,h)

    #calculating the new low and high index from the partition value
    if partition_val-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=partition_val-1

    if partition_val+1<h:
      top+=1
      stack[top]=partition_val+1
      top+=1
      stack[top]=h
  
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 


