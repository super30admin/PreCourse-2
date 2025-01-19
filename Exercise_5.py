""" 
Iterative QuickSort Implementation

# Time Complexity :
- Average case: O(n log n) where n is size of array
- Worst case: O(n²) when array is sorted/reverse sorted 
- Best case: O(n log n) with balanced partitions

# Space Complexity :
- O(log n) for the stack storing partition boundaries

"""

def partition(arr, low, high):
   pivot = arr[high]
   i = low - 1
   
   for j in range(low, high):
       if arr[j] <= pivot:
           i += 1
           arr[i], arr[j] = arr[j], arr[i]
   
   arr[i + 1], arr[high] = arr[high], arr[i + 1]
   return i + 1

def quickSortIterative(arr, low, high):
   stack = []
   
   stack.append((low, high))
   
   while stack:
       low, high = stack.pop()
       
       if low < high:
           pivot = partition(arr, low, high)
           
           if pivot - 1 > low:
               stack.append((low, pivot - 1))
               
           if pivot + 1 < high:
               stack.append((pivot + 1, high))

if __name__ == "__main__":
   arr1 = [10, 7, 8, 9, 1, 5]
   print("Original array:", arr1)
   quickSortIterative(arr1, 0, len(arr1) - 1)
   print("Sorted array:", arr1)
   assert arr1 == [1, 5, 7, 8, 9, 10]
   
   # Test case 2: Already sorted array
   arr2 = [1, 2, 3, 4, 5]
   quickSortIterative(arr2, 0, len(arr2) - 1)
   assert arr2 == [1, 2, 3, 4, 5]
   
   # Test case 3: Array with duplicates
   arr3 = [4, 2, 4, 1, 3, 4]
   quickSortIterative(arr3, 0, len(arr3) - 1)
   assert arr3 == [1, 2, 3, 4, 4, 4]
   
   # Test case 4: Single element
   arr4 = [1]
   quickSortIterative(arr4, 0, len(arr4) - 1)
   assert arr4 == [1]
   
   # Test case 5: Empty array
   arr5 = []
   quickSortIterative(arr5, 0, len(arr5) - 1)
   assert arr5 == []
   
   print("All test cases passed!")