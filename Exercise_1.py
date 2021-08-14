# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x): 
  
    #if empty
    if (r==0):
        return -1
    
#    print(l,r,x)
        
    while (l<=r):
        #mid has to be an integer, incase this was an array with 6 digits, it would be 2.5 and we would get 2
        mid = int((r+l)/2)
#        print("loop ",mid,l,r)
        #checking key with the middle element
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
#            print("in loop1")
            r = mid-1
        elif(arr[mid]<x):  
#            print("in loop2")
            l = mid+1
#    
    #if we complete the whole while loop but do not find, we reach here,
    return -1
  
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
 
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)
  
if result != -1: 
    print ("Element is present at index ", result) 
else: 
    print ("Element is not present in array")
