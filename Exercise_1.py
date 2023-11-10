# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n)
# Space Complexity : O(1)

def binarySearch(arr, l, r, x): 
  
  #write your code here

  while(l <= r): #As long as the left index does not become greater than the right index
    mid = int(l + (r-l)/2) #Mid is calculated this way to avoid integer overflow in case of other languages such as Java. It is the best practice, hence has been used here in Python
    if(arr[mid] == x): #If element at the mid index is the target, return the mid index
      return mid
    elif(x < arr[mid]): #If target is less than the element at mid, we move our search towards the left side because the input array is sorted, thus reducing the search space by half
      r = mid - 1
    else: #If target is greater than the element at mid, we move our search towards the right side, thus reducing the search space by half
      l = mid + 1
  return -1 #Target not found
  
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 40
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index % d" % result) 
else: 
    print("Element is not present in array")
