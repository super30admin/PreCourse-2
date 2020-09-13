# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
#Code Written by: Srinidhi Bhat
#Time Complexity - O(logN) - At every step we reduce search space by a factor of 2
#hence in logN steps we will be completing the search

#Space Complexity - O(1) - At max extra soace is used to store the mid element varialble which is constant
def binarySearch(arr, l, r, x):
	while l<=r:
		mid = (l+r)//2
		if arr[mid] == x:
			return mid+1
		else:
			if arr[mid] > x:
				r = mid -1
			else:
				l = mid + 1
	return -1
#def binarySearchRecursive():

  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
