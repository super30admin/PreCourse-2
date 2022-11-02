"""
	Problem Statement: Implement quick sort with recursive approach.

	Time Complexity: 
	partition(): O(n log n) on average case else O(n^2) worst case
	quick_sort(): O(n)

    Space Complexity:
    Auxiliary Space: O(1)

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

def quick_sort(arr, low, high): 
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
  
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Input array: ")
    print(*arr)

    n = len(arr)
    quick_sort(arr, 0, n-1) 
    
    print("Sorted array is:") 
    print(*arr)
 
