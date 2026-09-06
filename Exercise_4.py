"""
Time: O(n log n) in all cases (same halving + linear merge structure)
Space: O(n) auxiliary space (each recursive call still creates new sliced lists)

# Approach:
1. Divide the array into two halves
2. Recursively sort the left half
3. Recursively sort the right half
4. Merge the two sorted halves back into the original array
"""

# Python program for implementation of MergeSort 

def mergeSort(arr):
  
  #write your code here
  if arr is None or len(arr) < 2:
    return arr  # Already sorted or invalid input
  left = 0
  right = len(arr) - 1
  mid = left + (right - left) // 2
  left_half = arr[left:mid + 1]
  right_half = arr[mid + 1:right + 1]
  mergeSort(left_half)
  mergeSort(right_half)
  i = j = k = 0
  while i < len(left_half) and j < len(right_half):
    if left_half[i] <= right_half[j]:
      arr[k] = left_half[i]
      i += 1
    else:
      arr[k] = right_half[j]
      j += 1
    k += 1
  while i < len(left_half):
    arr[k] = left_half[i]
    i += 1
    k += 1
  while j < len(right_half):
    arr[k] = right_half[j]
    j += 1
    k += 1
  return arr
  
# Code to print the list 
def printList(arr): 
    if arr is None or len(arr) == 0:
        print("[]")
        return
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()  # New line at the end

  
def run_test():
    test_cases = [
        ("Unsorted array", [12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),
        ("Already sorted", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ("Duplicates", [4, 2, 2, 8, 4, 1], [1, 2, 2, 4, 4, 8]),
        ("Single element", [42], [42]),
        ("Empty array", [], []),
        ("Two elements", [2, 1], [1, 2]),
        ("Negative numbers", [-3, -1, -7, 2, 0], [-7, -3, -1, 0, 2]),
        ("All same elements", [7, 7, 7, 7], [7, 7, 7, 7]),
        ("None input", None, None),
    ]

    for name, input_arr, expected in test_cases:
        result = input_arr[:] if input_arr is not None else None  # copy so original isn't mutated
        result = mergeSort(result)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {name} -> got {result}, expected {expected}")


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)

    print("\nRunning tests...")
    run_test()
    print("\nAll tests completed.")
