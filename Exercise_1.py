# Python code to implement iterative Binary Search.
#Time Complexity: O(log n)
#Space Complexity: O(1)
# It returns location of x in given array arr
# if present, else returns -1
def binarySearch(arr, l, r, x):
	#check base case
	if r >= l:
		# calculating mid
		mid = (l + r) // 2
		#if mid is equal to target return mid
		if arr[mid] == x: 
			return mid
		#if mid is less than target, search on the left
		elif arr[mid] > x:
			return binarySearch(arr, l, mid - 1, x)
		#if mid is greater than target, search right
		elif arr[mid] < x:
			return binarySearch(arr, mid + 1, r, x)
	else:
		# if the element is not present in arr
		return -1

# Test array
arr = [2, 3, 4, 10, 40 ] 
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print ("Element is present at index % d" % result)
else:
    print("Element is not present in array")
