def binarySearch(arr,first,last,element):
	if last >= 1:
		mid = first + int((last - first)/2)
		if arr[mid] == element:
			return mid
		elif arr[mid] > element:
			return binarySearch(arr,first,mid-1,element)
		elif arr[mid] < element:
			return binarySearch(arr,mid+1,last,element)
	else:
		return -1


''' Driver Code'''
arr = [1,5,7,9,13,16,20,25,43,50,61,65,70,73,79,80,83,85,89,95]
element_to_find = 50

ans = binarySearch(arr, 0, len(arr)-1, element_to_find)

if ans != -1: 
    print("Element is present at index %d" %ans ) 
else: 
    print("Element is not present in array")