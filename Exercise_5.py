#//Time Complexity :O(nlogn)
#// Space Complexity : O(logn) 
#// Did this code successfully run on Leetcode : No
#// Any problem you faced while coding this :Had difficulty in converting logic to code.
# Python program for implementation of Quicksort Sort 

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    i = l - 1
    pivot = arr[h]
    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1



def quickSortIterative(arr, l, h):
  #write your code here
  # Create an auxiliary stack
  size = h -l + 1
  stack = [0] * size 
  top = -1
  stack[top] = l
  top += 1
  stack[top] = h
  
  #keep popping until it is empty
  while top >= 0:
   h = stack[top]
   top -= 1
   l = stack[top]
   top -= 1

   #setting pivot element position
   p = partition(arr, l, h)

    #elemnets on left side of pivot push left side of stack
   if p -1 > l:
      top += 1
      stack[top] = l
      top += 1
      stack[top] = p - 1

    #elemnts on right side of pivot push ot right sode of the stack
   if p + 1 < h:
      top += 1
      stack[top] = p + 1
      top +=1
      stack [top] = h


if __name__ == "__main__":
    # Sample array to test
    data = [10, 7, 8, 9, 1, 5]
    n = len(data)
    print("Original array:", data)
    # l is 0 (start index) and h is n-1 (last index)
    quickSortIterative(data, 0, n - 1)
    print("Sorted array:  ", data)