#Space Complexity: O(n) ... where n is the number of elements
#Time Complexity: O(n log n) ... where n is the number of elements
#Faced issues while implementing the stack in order to 

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot = arr[h]                           #taking the last element as the pivot
  i = l - 1                                 #this is to mark the posiiton from where the partition starts
  j = l
  while j < h:
      if arr[j] <= pivot:
          i += 1
          arr[i],arr[j] = arr[j],arr[i]       #done to adjust the oeft half partition elements
      j += 1
  
  arr[i+1],arr[h] = arr[h],arr[i+1]     #to place the pivot at the correct position(which is after the partition point)
  return i + 1

def quickSortIterative(arr, l, h):
    temp = [0] * len(arr)               #creating a temp stack to store the start and end pointers for each subsequent divisions

    top = 0
    temp[top] = l
    top += 1
    temp[top] = h
    
    while top > -1:
 
        h = temp[top]
        top -= 1
        l = temp[top]
        top -= 1
 
        p = partition( arr, l, h )      #finding the pivot and putting it at the correct position
        
        if p-1 > l:                     #checking if pivot has any elements in the left half division and if so then adding that left half's start and end pointers to the temp stack
            top += 1
            temp[top] = l
            top += 1
            temp[top] = p - 1
 
        if p+1 < h:                     #checking if pivot has any elements in the right half division and if so then adding that right half's start and end pointers to the temp stack
            top += 1
            temp[top] = p + 1
            top += 1
            temp[top] = h
