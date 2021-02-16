# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
  #write your code here
    while l<=r:
        mid = int((l+r)/2)
        #print(arr[mid])
        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            return mid
    return -1


    
  
# Test array 
arr = [ 1 ]
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1: 
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
