# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode: I ran this code in VS Code editor in my local machine
# Any problem you faced while coding this: No

# Python code to implement iterative Binary  Search. 
  
# It returns location of x in given array 'arr' if present, else returns -1 
def binarySearch(arr, l, r, x):
    
    # If algo reaches end of the array and don't find the element
    if l > r:
        return -1
    else:
        # Divide the array in half and get the middle index
        mid = (l + r) // 2

        # If element at middle index is the target element
        if arr[mid] == x:
            return mid
        # If element at middle index is less than the target element, search the right half of the array
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, r, x)
        # Else if element at middle index is greater than the target element, search the left half of the array
        else:
            return binarySearch(arr,l,mid-1, x)
 
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
