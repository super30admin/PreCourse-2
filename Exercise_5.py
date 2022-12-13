# Time Complexity : 0(n*log(n))
# Space Complexity :O(1)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this :No

# Python program for implementation of Quicksort
from collections import deque
# This function is same in both iterative and recursive
def partition(arr, low, high):
  p = arr[high]
  lower = 0
  for j in range(high):
    if(arr[j]<p):
      (arr[lower],arr[j])=(arr[j],arr[lower])
      lower+=1
  (arr[lower],arr[high])=(arr[high],arr[lower])
    
  return lower


def quickSortIterative(arr):
   
  stack = deque() # A stack for storing sublist's start and end index
  (start,end)=(0,len(arr)-1)
 
  stack.append((start, end)) # Append the start and end index of the main array

  while stack:  # loop till stack is empty
    start, end = stack.pop()
 
    pivot = partition(arr, start, end)  # Partition elements across pivot
 
    if pivot - 1 > start:
      stack.append((start, pivot - 1)) #Append the start and end index of the sub arrays if they are within bound
    if pivot + 1 < end:
      stack.append((pivot + 1, end))
  return(arr)

arr = [12, 11, 13, 5, 6, 7]  
print ("Given array is", end="\n")  
print(arr) 
arr=quickSortIterative(arr) 
print("Sorted array is: ", end="\n") 
print(arr) 
