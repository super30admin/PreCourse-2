# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

#TimeComplexity: O(log n)
#SpaceComplexity: O(n)

def binarySearch(arr, l, r, x): 
  
    #check if the array has any more elements left to check otherwise return -1
    if r>=l:
        mid = (l+r)//2
        #if x matched the middle element return middle index
        if x == arr[mid]:
            return mid
        #if x in smaller search in the left side of the array
        elif arr[mid]>x:
            return binarySearch(arr, l, mid-1, x)
        #if x is greater search in the right side of the array
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
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
