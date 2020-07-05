# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

""" This program is written with the assumption that the input array is sorted.
Time complexity is  O(log n). The length of the array is reduced by half in each iteration until it becomes 1.
The number of iterations required so that the list only contains one element is log n.
The space complexity is constant O(1) since only start, end, mid variables are needed. """

def binarySearch(arr, l, r, x): 
  
  #write your code here
  	if(l<=r):
	  mid = l + ((r-l)//2)
	  if(arr[mid] == x):
	  	return mid
	  elif(arr[mid] > x):
	  	return binarySearch(arr,l,mid-1,x)
	  else:
	  	return binarySearch(arr,mid+1,r,x)
	return -1

    
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print "Element is present at index % d" % result 
else: 
    print "Element is not present in array"
