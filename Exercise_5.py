# Python program for implementation of Quicksort
# // Time Complexity : O(nlogn)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Not Found
# // Any problem you faced while coding this : 


# // Your code here along with comments explaining your approach
# In this took the end element as the pivot. 
# Sorted the left sub array and right sub array when divided by pivot in its correct place.

# This function is same in both iterative and recursive
def partition(arr, l, h):
    startIndex = (l - 1)         #smaller element
    pivot = arr[h]     #pivot
    for j in range(l, h):  #Compare current element with pivot 
		if arr[j] <= pivot:
			startIndex += 1
			arr[startIndex], arr[j] = arr[j], arr[startIndex]
	arr[startIndex + 1], arr[h] = arr[h], arr[startIndex + 1]
    return (startIndex + 1)

def quickSortIterative(arr, l, h):
	if l < h:
        partIndex = partition(arr, l, h)
        quickSortIterative(arr, l, partIndex -1)
        quickSortIterative(arr, partIndex + 1, h)
  

if __name__ == '__main__' :
    arr = [6, 3, 1, 4, 9, 12]
    n = len(arr)
    quickSortIterative(arr, 0, n - 1)
    for i in range(n):
        print(arr[i], end = " ")

