# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
"""
Time Complexity:
  partition()          : O(n) 
  quickSortIterative() - Best Case & Average Case     : O(n log n)
  quickSortIterative() - Worst Case   : O(n^2)  

Space Complexity:
  Worst case         : O(n)
  Best/Average case  : O(log n)  
"""

def partition(arr, low, high):
  #write your code here
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSortIterative(arr, l, h):
  #write your code here
    stack = []
    stack.append(l)
    stack.append(h)
    while stack:
        h = stack.pop()
        l = stack.pop()
        pivot = partition(arr,l,h)
        if (pivot-1>l) :
            stack.append(l)
            stack.append(pivot-1)
        if(pivot+1<h):
            stack.append(pivot+1)
            stack.append(h)



# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]

n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),