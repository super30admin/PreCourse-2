# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity: O(log n)
# Space Complexity: O(1)

def binarySearch(arr, l, r, x): 
  
  #write your code here

  while l < r or l == r:
     mid = l+(r-l)//2
     print(l, r, mid)
     if x == arr[mid]:
        return mid
     elif x > arr[mid]:
        l = mid + 1      
     else:
        r = mid - 1
  return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
    print ("Element is present at index: ", result )
else: 
    print ("Element is not present in array")
