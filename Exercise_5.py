# Python program for implementation of Quicksort
#Time Complexity:- O(n log n)
#Space Complexity:- O(log n)
# This function is same in both iterative and recursive
def partition(arr, l, h):
  pivot=arr[h]
  i=i-1

  #Iterate through the subarray from index 1 to h-1
  for j in range(l,h):
    if arr[j]<=pivot:
       i+=1
       arr[i], arr[j]=arr[j], arr[i] #Swap elements

  #Swap the pivot element to its correct position
  arr[i+1], arr[h]= arr[h], arr[i+1]
  return i+1 #Return the index of the pivot element

def quickSortIterative(arr, l, h):
  stack=[(l,h)] #Create a stack to store subarray indices

  while stack:
     l,h=stack.pop() #Pop a subarray from the stack

     if l<h:
        pivot_index=partition(arr,l,h) #Partition the subarray

        #Push the subarrays before and after the pivot onto the stack
        stack.append((l, pivot_index-1)) #Left Subarray
        stack.append((pivot_index+1,h))  #Right Subarray



