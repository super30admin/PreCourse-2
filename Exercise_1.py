# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, left, right, x): 
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1

 
arr = [2, 3, 4, 10, 40] 
x = 50
  
result = binarySearch(arr, 0, len(arr) - 1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
