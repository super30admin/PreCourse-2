# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    m = (l+r)//2
    if x == arr[m]:
        return m
    elif x > arr[m]:
        return binarySearch(arr, m+1, r, x)
    elif x < arr[m]:
        return binarySearch(arr, l, m-1, x)
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print(f"Element is present at index :{result}")
else: 
    print("Element is not present in array")
