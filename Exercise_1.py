# PreCourse_2: Exercise_1 : Python code to implement iterative Binary Search

#Linear Search will be of O(n) time complexity.
#The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
#Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty. We basically ignore half of the elements just after one comparison.

# It returns location of x in given array arr  
# if present, else returns -1 


def binarySearch(arr, l, r, x): 
  if r >= l:    #base case
    mid = (l + r) // 2
    if arr[mid] == x:
      return mid
    elif arr[mid] > x:
      return binarySearch(arr, l, mid-1, x)
    else:
      return binarySearch(arr, mid+1, r, x)
  else:
    return -1

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
