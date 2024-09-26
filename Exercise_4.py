# Python program for implementation of MergeSort 
"""
Time - O(nlogn) logn to divide and n to merge
Space - O(n) as we are making copy of array
Idea - First we keep on dividing the array into half and then it is merged again in ascending order
"""
def mergeSort(arr): 
  divide(arr, 0, len(arr)-1)

def divide(arr, start, end): # time - O(logn)
  if start >= end:
    return

  midpoint = (start + end) // 2 + 1

  divide(arr, start, midpoint-1)
  divide(arr, midpoint, end)

  merge(arr, start, midpoint, end)

def merge(arr, start, start2, end): # time - O(n)
  p1 = start
  p2 = start2
  cur = start
  copy = arr[:]

  while cur <= end:
    if p1 < start2 and p2 <= end:
      if copy[p1] < copy[p2]:
        arr[cur] = copy[p1]
        p1 += 1
      
      else:
        arr[cur] = copy[p2]
        p2 += 1
    
    elif p1 < start2:
      arr[cur] = copy[p1]
      p1 += 1

    else:
      arr[cur] = copy[p2]
      p2 += 1
    
    cur += 1

      
  
  
# Code to print the list 
def printList(arr): 
  print(arr)
    
    
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
