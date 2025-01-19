""" 
Exercise_2 : Quick sort.

# Time Complexity :
- Average case: O(n log n) where n is the size of array
- Worst case: O(n²) when array is already sorted in reverse
- Best case: O(n log n) when partition always picks middle element

# Space Complexity :
- O(log n) average case for recursion stack
- O(n) worst case for recursion stack when array is sorted/reverse sorted

"""

def partition(arr, low, high):
    pivot = arr[high]    
    i = low - 1     

    # swap elements smaller than pivot to left of pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    
    # swap pivot with element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        
        # Divide and conquer
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

# Tests
if __name__ == "__main__":
    # Test case 1: Random array
    arr1 = [10, 7, 8, 9, 1, 5]
    n1 = len(arr1)
    quickSort(arr1, 0, n1-1)
    assert arr1 == [1, 5, 7, 8, 9, 10]
    
    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    n2 = len(arr2)
    quickSort(arr2, 0, n2-1)
    assert arr2 == [1, 2, 3, 4, 5]
    
    # Test case 3: Array with duplicates
    arr3 = [4, 2, 4, 1, 3, 4]
    n3 = len(arr3)
    quickSort(arr3, 0, n3-1)
    assert arr3 == [1, 2, 3, 4, 4, 4]
    
    # Test case 4: Single element array
    arr4 = [1]
    quickSort(arr4, 0, 0)
    assert arr4 == [1]
    
    print("All test cases passed!")