# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
    #write your code here
    while l < r:
        m = l + (r - l) // 2
        print(m, arr[m], x)
        if x < arr[m]:
            r = m - 1
        elif x > arr[m]:
            l = m + 1
        else:
            return m
    return -1

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1:
    print("Element is present at index %d" % result)
else: 
    print("Element is not present in array")
