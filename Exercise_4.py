""" 
Merge Sort Implementation

# Time Complexity :
- O(n log n) for all cases (best, average, worst)
- log n levels of recursion
- n comparisons at each level during merge

# Space Complexity :
- O(n) auxiliary space for storing temporarily merged arrays
- O(log n) for recursion stack

"""

def mergeSort(arr):
   if len(arr) > 1:
       mid = len(arr) // 2
       
       L, R = arr[:mid], arr[mid:]
       
       mergeSort(L)
       mergeSort(R)
       
       i = j = k = 0
       
       while i < len(L) and j < len(R):
           if L[i] <= R[j]:
               arr[k] = L[i]
               i += 1
           else:
               arr[k] = R[j]
               j += 1
           k += 1
           
       while i < len(L):
           arr[k] = L[i]
           i += 1
           k += 1
           
       while j < len(R):
           arr[k] = R[j]
           j += 1
           k += 1

def printList(arr):
   for i in range(len(arr)):
       print(arr[i], end=" ")
   print()

# Driver code
if __name__ == '__main__':
   # Test case 1: Random array
   arr = [12, 11, 13, 5, 6, 7]
   print("Given array is", end="\n")
   printList(arr)
   mergeSort(arr)
   print("Sorted array is: ", end="\n")
   printList(arr)
   assert arr == [5, 6, 7, 11, 12, 13]
   
   # Test case 2: Already sorted array
   arr2 = [1, 2, 3, 4, 5]
   mergeSort(arr2)
   assert arr2 == [1, 2, 3, 4, 5]
   
   # Test case 3: Array with duplicates
   arr3 = [4, 2, 4, 1, 3, 4]
   mergeSort(arr3)
   assert arr3 == [1, 2, 3, 4, 4, 4]
   
   print("All test cases passed!")