# Python program for implementation of MergeSort

"""
    Merge Sort takes O(n log n) for any input
    where n is total numbers the input array
"""
def mergeSort(arr):
    # write your code here
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    mergeList(left, right, arr)


def mergeList(left, right, arr):
	lenLeft = len(left)
	lenRight = len(right)

	l = r = k = 0

	while l < lenLeft and r < lenRight:
		if left[l] <= right[r]:
			arr[k] = left[l]
			l += 1
		else:
			arr[k] = right[r]
			r += 1
		k += 1
		
	while l < lenLeft:
		arr[k] = left[l]
		l += 1
		k += 1

	while r < lenRight:
		arr[k] = right[r]
		r += 1
		k += 1

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 2, 1]
    print(f"Given array is {arr} \n")
    mergeSort(arr)
    print(f"Sorted array is{arr}")
