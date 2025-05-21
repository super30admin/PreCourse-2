# Python program for implementation of Quicksort
#Time Complexity:
# Best Case, Average Case:O(n log n)- as array is divided and sorted.
# Worst Case:O(n^2)- Happens when pivot selection leads to unbalanced partitons
#Space Complexity:
# Average Case: O(log n)-Stack stores log n subarray ranges
# Worst Case: O(n)-if stack grows due to pivot choices
# This function is same in both iterative and recursive
#Did this code successfully run on Leetcode :Yes
def partition(arr, l, h):
  #write your code here
  pivot=arr[h]
  i=l-1
  for j in range (l,h):
    if arr[j]<=pivot:
      i+=1
      arr[i],arr[j]=arr[j],arr[i] #swaps if smaller or equal
  arr[i+1],arr[h]=arr[h],arr[i+1] #places pivot at correct position
  return i+1

def quickSortIterative(arr, l, h):
  #write your code here
  stack=[]
  stack.append((l,h)) #pushes the initial range
  while stack:
    l,h=stack.pop()
    if l<h:
      p=partition(arr,l,h)      #partitions the array and gets pivot index
    if p-1>l:                   #if the left part of the pivot has more than one element,push to stack
      stack.append((l,p-1))
      if p+1<h:                 #if the right part has more than one element,push to stack
        stack.append((p+1,h))

if __name__=='__main__':     #code to test
  arr=[1,3,6,8,5,6,7,9]
  print("Array is")
  print(*arr)
  quickSortIterative(arr,0,len(arr)-1)
  print("Sorted array is")
  print(*arr)