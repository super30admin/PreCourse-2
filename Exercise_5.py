"""  
 
 Time Complexity : worst case is O(n^2) Average cases is O(nlogn)
 Space Complexity : worst case is O(n) Average cases is O(nlogn) (space is calculated on call stack size)
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : No


 Your code here along with comments explaining your approach :
 First we're storing the tuple of arr,low,high combination in a stack list to replicate the recursive behavior. We'll loop the stack until it's empty and pop the element & execute the partion logic i.e., checking the left and right boundaries and if they fall in between them then we're taking pivot as high index element
 and we're checking if any element is smaller or equal to pivot if yes then we're incrementing i which is nothing but the least index where
 we previously left i.e. initially low and swapping the ith index to jth index. We're repeating this process from low to high and after that we're swapping
 the high with the i+1 index and return i+1 as the partion done based on this. Now in the next subsequent calls we'll split the left array before partition and
 right array after partition and push it to stack and repeat the same process of finding the pivot by poping one by one from stack until we reach the end. 
 
 """
 
 # Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  pivot = arr[h]
  i = l - 1

  for j in range(l,h):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i+1], arr[h] = arr[h], arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  
  stack = [(arr, l, h)]

  while len(stack) > 0:
    arr, l, h = stack.pop()
    if l < h:
      pivot = partition(arr, l, h)
      stack.append((arr, l, pivot - 1))
      stack.append((arr, pivot + 1, h))

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


