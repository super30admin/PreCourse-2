"""
Problem - Find and return location of target in given array if present, else return -1 using Iterative Binary Search
Example - Input - numbers = [2, 3, 4, 10, 40], target = 10
          Output - 3
Solution - Iterative Binary Search using two pointers
Time Complexity - O(log n) where n is number of elements in the given array
Space Complexity - O(1)
Test Cases - Edge Cases - Empty array, target not present, duplicates
             Base Cases - Array with 1 element, 2 elements
             Regular Cases - array with many elements having target
"""


# Function to find index of target element in an array
def find_index_by_binary_search(numbers, target):
    if numbers is None or len(numbers) < 1:
        return -1

    left = 0
    right = len(numbers)-1

    while left <= right:
        mid = int(left + (right - left) / 2)
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        elif numbers[mid] > target:
            right = mid - 1
    return -1


# Driver code
numbers = [2, 3, 4, 10, 40]
target = 10
result = find_index_by_binary_search(numbers, target)

if result != -1: 
    print("Element is present at index", result)
else: 
    print("Element is not present in array")
