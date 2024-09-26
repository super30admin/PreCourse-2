# // Time Complexity : O(NlogN)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : No 


# // Your code here along with comments explaining your approach
"""
1. Partition function will calculate the pivot index as middle index and find right position for it , return the index 
2. will maintain a stack , loop through untill its empty 
3. will pop two elements from stack l and h , once we get index for the pivot from partition func , will push new l and h based and the pivot index 

"""



# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):

  #write your code here
  pivot = (l + h) //2 
  arr[pivot] , arr[h] = arr[h] , arr[pivot]

  for each in range(l,h):
      if arr[each] <= arr[h]:
          arr[each],arr[l] = arr[l], arr[each]
          l += 1
  arr[l], arr[h] = arr[h], arr[l]
  return l 



def quickSortIterative(arr, l, h):
  #write your code here
  stack =[]

  stack.append(l)
  stack.append(h)

  while len(stack):
    l = stack.pop(0)
    h = stack.pop(0)
    pivot = partition(arr, l , h)
    if pivot - 1 > l:
      stack.append(l)
      stack.append(pivot - 1)
    if pivot + 1 < h:
      stack.append(pivot + 1)
      stack.append(h)
      
    



# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 