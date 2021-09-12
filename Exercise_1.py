# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
    found = False
    

    while not found and l <= r:

        index = int((l+r) / 2)
        # print(l,r,index)
        if arr[index] == x:
            return index
        elif arr[index] < x:
            l = index + 1
        else:
            r = index - 1
    return -1


  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result )
else: 
    print ("Element is not present in array")
