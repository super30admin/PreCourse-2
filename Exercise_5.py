# Time Complexity : O(nlogn)
# Space Complexity : O(1)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  pivot = low
  i = low
  j = high

  while (i < j):
      while(arr[i] < arr[pivot] and i <= high):
          i += 1
      while (arr[j]> arr[pivot] and j >= low):
          j -= 1
      if (i < j):
          arr[i],arr[j] = arr[j],arr[i]
  arr[pivot],arr[j] = arr[j],arr[pivot]
  return j
    


def quickSortIterative(arr, low, high):
  #write your code here
    if len(arr) == 0:
       return
    stack = [(0, len(arr)-1)]
    while (stack):

        low,high = stack.pop()
        j = partition(arr,low, high)

        if low < j-1:
          stack.append((low, j-1))
        if j+1 < high:
          stack.append((j+1, high))



# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

