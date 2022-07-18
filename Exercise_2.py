# Python program for implementation of Quicksort Sort 
# Recursive approach 

#  Time complexity : O(nlogn)
#  Space Complexity : O(1)


# give you explanation for the approach
def partition(arr,low,high):
#   Arr's right element is the pivot here and arr's low is the ptr
  #write your code here
  pivot, ptr = arr[high],low
  for i in range(low,high):
    if arr[i] <= pivot:
      arr[i], arr[ptr] = arr[ptr], arr[i]
      ptr += 1

    arr[ptr], arr[high] = arr[high], arr[ptr]
  return ptr



# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    
  if len(arr) == 1:
    return arr

  if low < high :
    part = partition(low,high,arr)
    # Recursively sort left values
    quickSort(low, part-1, arr)
    # Recursively sort right values   
    quickSort(part+1, high,arr)

  return arr

 
