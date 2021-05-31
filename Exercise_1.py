# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1



# Time Complexity : O(logn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :

# Below function is recursive function
# Function 1
def binarySearch(arr, l, r, x):
    mid_element = (l + r)/2

    if arr[mid_element] == x:
        return mid_element

    if arr[mid_element] > x:
       return binarySearch(arr, 0, mid_element, x)

    elif arr[mid_element] < x:
        return binarySearch(arr, mid_element + 1, r, x)

#  Below is while loop implementation
# Function 2
def binarySearch1(arr, l, r, x):

    while l <= r:

        mid_index = (l + r)/2

        if arr[mid_index] == x:
            return mid_index

        if arr[mid_index] > x:
            r = mid_index

        if arr[mid_index] < x:
            l = mid_index + 1


  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
result1 = binarySearch1(arr, 0, len(arr)-1, x)

if result != -1: 
    print ("Element is present at index in Function 1", result)
    print ("Element is present at index in Function 2 ", result1)
else:
    print "Element is not present in array"
