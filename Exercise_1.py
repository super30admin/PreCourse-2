# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):
    while l <= r:
        middle = (l+r)//2 
        print (l)
        print (r)
        print (x)
        print (middle)
        if x == arr[middle]:
            return middle
        elif x < arr[middle]:
            r = middle - 1 
        else:
            l = middle + 1
    return -1
            
    
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")


