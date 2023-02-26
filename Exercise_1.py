# Python code to implement iterative Binary  
# Search. 
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O(log n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


def binarySearch(arr, l, r, x): 
  
  #write your code here
  
	while l < r:
		mid = (l+r)//2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
				r-=1
		else:
			l+=1	
	return -1
    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 55
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index ",result )
else: 
    print("Element is not present in array")
