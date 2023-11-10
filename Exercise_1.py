# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = int((high + low) / 2)
		if arr[mid] < x:
			low = mid + 1

		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 4

res = binary_search(arr, x)

if res != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
