"""
	Problem Statement: Implement quick sort with iterative approach.

	Time Complexity: 
	quick_sort(): O(n log n)

    Space Complexity:
    Auxiliary Space: O(n) since we are using stack

"""
def partition(arr,low,high):
	pivot = arr[high]
	idx = low - 1

	for i in range(low, high):
		if arr[i] <= pivot:
			idx += 1
			arr[idx], arr[i] = arr[i], arr[idx]
	arr[idx + 1], arr[high] = arr[high], arr[idx + 1]
	return idx + 1


def quick_sort_iterative(arr, low, high):
    size = high - low + 1
    stack = [0] * size
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
 
        pivot = partition(arr, low, high)
 
        if (pivot - 1) > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = pivot - 1
 
        if (pivot + 1) < high:
            top += 1
            stack[top] = pivot + 1
            top += 1
            stack[top] = high

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Input array: ")
    print(*arr)

    n = len(arr)
    quick_sort_iterative(arr, 0, n-1) 
    
    print("Sorted array is:") 
    print(*arr)