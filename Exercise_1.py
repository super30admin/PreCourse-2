# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
    # find the mid iteratively ab=nd if the element matches , return index else
    # move the index to left or right based on whether the number at current index is greater and smaller respectively
    while(l <= r):
        mid =  (r+l) // 2
        if arr[mid] == x:
            return mid
        elif (arr[mid] < x):
            l = mid + 1
        # this is arr[mid] > x
        else:
            r = mid - 1
    # return -1 if there is no "return mid " from above while loop
    return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"


