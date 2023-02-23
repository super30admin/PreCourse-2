# Python program for implementation of Quicksort

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
    pivot = arr[h] #pivot is selected as the last element in the list
    i = l - 1 #set to the smaller number

    for j in range(l, h):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[h]) = (arr[h], arr[i+1])

    return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
  stack = []
  stack.append((l, h))

  while stack:
      start, end = stack.pop()

      pi = partition(arr, start, end)

      if pi - 1 > start:
          stack.append((start, pi - 1))

      if pi + 1 < end:
          stack.append((pi + 1, end))


# Driver code to test above 
arr = [10, 41, 7, 8, 9, 1, 5, -1] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 