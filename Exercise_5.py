# Time Complexity :   Here the time complexity is of O(n log n)
# Space Complexity :  Since we are using stack data structure here the Time complexity is O(n)
# Did this code successfully run on Leetcode : Did not try running code on leetcode as the question and inputs on leetcode are bit different.
# Any problem you faced while coding this : Issues faced to implement using stack data structure


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]                                      #taking last element as the pivot
  i, j = l, h - 1
  while i < j:
      while i < h and arr[i] < pivot:                 # i looks for element bigger than pivot, if elem at i < pivot then i is incremented
          i += 1                                      
      while j > l and arr[j] >= pivot:                # j looks for element smaller than pivot, if elem at j >= pivot then j is decremented
          j -= 1
      
      if i < j:                                       # if i < j then we swap the elements at i and j         
          arr[i], arr[j] = arr[j], arr[i]

  if arr[i] > pivot:                                  
      arr[i], arr[h] = arr[h], arr[i]

  return i                                            # returns the index of pivot where elements on left of i are less than pivot
                                                      # and elements to right of i are greaterd than pivot

def quickSortIterative(arr, l, h):
  #write your code here
  length = h - l + 1
  stack = [0] * (length)                              #creating a stack of size input length                            

  top = -1                                            #initializing top of stack to b -1
  
  top += 1                                            #incrementing the count of top and then pushing values l and h
  stack[top] = l
  top += 1
  stack[top] = h

  while top >= 0:                                     #remove elements from top of stack until its not empty
    h = stack[top]                                    #get the corresponding l and h values from stack by pop
    top -= 1
    l = stack[top]
    top -= 1

    pivot = partition( arr, l, h )                    #set the pivot at correct index in the array where left elements are < pivot and right elements are > pivot

    if pivot-1 > l:                                   #if there are elements on left of pivot then we push l to pivot-1 to stack
      top += 1
      stack[top] = l
      top += 1
      stack[top] = pivot - 1

    if pivot+1 < h:                                   #if there are elements on right of pivot then we push pivot+1 to h to stack
      top += 1
      stack[top] = pivot + 1
      top += 1
      stack[top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
quickSortIterative(arr, 0, len(arr)-1)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])