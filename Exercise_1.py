# Python code to implement iterative Binary  
# Search. 
	
# It returns location of x in given array arr  
# if present, else returns -1 

"""
Intuition:  The array in which the element is search can be reduced in half for every iteration
This reduction in size can be performned by checking if the element is present on the left half or right half of the array.
This will work only for sorted arrays

For iterative method:
Time Complexity : O(log n)
Space Complexity : O(1)

For recursive method:
Time Complexity : O(log n)
Space Complexity : O(log n)
"""
def binarySearch(array, leftIndex, rightIndex, key): 
	
	while leftIndex <= rightIndex:
		midIndex = (leftIndex + rightIndex)//2
		if key ==  array[midIndex]:
			return midIndex
		if key > array[midIndex]:
			leftIndex = midIndex + 1
		elif key 	< array[midIndex]:
			rightIndex = midIndex - 1
	return -1

def binarySearchRecursive(array, leftIndex, rightIndex, key): 
	midIndex = (leftIndex + rightIndex)//2

	#Base condition
	if key ==  array[midIndex]:
		return int(midIndex)
	
	else:
		if key > array[midIndex]:
			return binarySearchRecursive(array, midIndex + 1, rightIndex, key)
		else:
			return binarySearchRecursive(array, leftIndex, midIndex - 1, key)


# Test array 
arr = [ 2, 3, 4, 10, 40] 
x = 10
	
# Function call 
print("########################################")
print("Using Iterative Method!")
result = binarySearch(arr, 0, len(arr)-1, x) 
	
if result != -1: 
	print("Element is present at index % d" % result )
else: 
	print("Element is not present in array")

print("########################################")
print("Using Recursive Method!")
result = binarySearchRecursive(arr, 0, len(arr)-1, x) 
	
if result != -1: 
	print("Element is present at index", result )
else: 
	print("Element is not present in array")
