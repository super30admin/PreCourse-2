# Python program for implementation of Quicksort
# Time Complexity : O(log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : No. Could not find this problem on geeks or leetcode
# Any problem you faced while coding this : Yes. While implementing the Iterative sort logic.

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot_index = l
  pivot_element = arr[pivot_index]

  i = pivot_index + 1
  j = h

  while i <= j:
    while i <=j and arr[i] <= pivot_element:
      i += 1

    while i <=j and arr[j] >= pivot_element:
      j -= 1
    
    if i <=j:
      arr[i], arr[j] = arr[j], arr[i]

    arr[pivot_index], arr[j]  =  arr[j], arr[pivot_index]

    return j

def quickSortIterative(arr, l, h):
  #write your code here

    stack = []

    # append starting range to stack
    stack.append((l, h))

    # continue this operation until the stack is empty means all the elements are considered
    while stack:
        l, h = stack.pop()

        if l < h:
            # call the partition function and find the pivot element position(index)
            p = partition(arr, l, h)

            # get the left hand side element from the pivot element position(index)
            if p > l:
                stack.append((l, p))

            # get the right hand side element from the pivot element position
            if p + 1 < h:
                stack.append((p + 1, h))
    return arr

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("i",arr[i])