# Python code to implement iterative Binary  
# Search. 
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n) (best case O(1))
# Space Complexity : O(1)
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No

def binarySearch(arr, l, r, x): 

  # Binary search uses a sorted array. Setting up l = low and r = high. As long as low is less than high, searching array

  while l <= r:                

    # setting up a mid at the center
    mid = ( l + r ) // 2        

    # case 1: if value at mid index is greater than x, means x has to be on the left. Hence high = mid - 1
    if ( arr[mid] > x ):        
      r = mid - 1

    # case 2: if value at mid index is less than x, x has to be on the right. low = mid + 1  
    elif ( arr[mid] < x ):      
      l = mid + 1

    # case 3: if value at mid index is = x then mid = x
    else:                       
      return mid

  # break while loop    
  return -1                      

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" %result)
else: 
    print ("Element is not present in array")
