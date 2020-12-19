# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
  #write your code here
    if r >= l: 

        mid = (r + l) // 2

        if arr[mid] == x: 
            return mid 

        # Checking left 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid - 1, x) 

        # checking right
        else: 
            return binary_search(arr, mid + 1, r, x) 

    else: 
        # Element is not present in the array 
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
