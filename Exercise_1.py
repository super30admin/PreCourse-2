# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x) ->  int:
  #write your code here
    if l <= r:
        mid = l + (r-l) // 2
        if arr[mid] == x:
            print("Element is present at index ",mid)
            return mid
        elif arr[mid] < x:
            binarySearch(arr, mid+1, r, x)
        else:
            binarySearch(arr, l, mid-1, x)
    else:
        return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
if result != -1: 
    print ("Element is present at index ", str(result))
else: 
    print ("Element is not present in array")
