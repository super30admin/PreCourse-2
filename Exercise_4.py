"""
	Problem Statement: Implement merge sort.

	Time Complexity: 
	partition(): O(n log n)
	quick_sort(): O(n)

    Space Complexity:
    Auxiliary Space: O(1)

"""

def mergeSort(arr, left, right):
	if left < right:
		mid = (left + right) // 2
		mergeSort(arr, left, mid)
		mergeSort(arr, mid + 1, right)
		merge(arr, left, mid, right)


def merge(arr, left, mid, right):
	left_arr_length = mid - left + 1
	right_arr_length = right - mid;
	
	left_arr = [0] * left_arr_length
	right_arr = [0] * right_arr_length

	for idx in range(0, left_arr_length):
		left_arr[idx] = arr[left + idx]

	for idx in range(0, right_arr_length):
		right_arr[idx] = arr[mid + idx + 1]

	left_idx, idx, right_idx = 0, left, 0

	while left_idx < left_arr_length and right_idx < right_arr_length:
		if left_arr[left_idx] <= right_arr[right_idx]:
			arr[idx] = left_arr[left_idx]
			left_idx += 1
		else:
			arr[idx] = right_arr[right_idx]
			right_idx += 1
		idx += 1

	while left_idx < left_arr_length:
		arr[idx] = left_arr[left_idx]
		left_idx += 1
		idx += 1

	while right_idx < right_arr_length:
		arr[idx] = right_arr[right_idx]
		right_idx += 1
		idx += 1

def print_list(arr):
	"""Display items in the array"""
	for item in arr:
		print(item, end=" ")
	print()
  
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print_list(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    print_list(arr) 
