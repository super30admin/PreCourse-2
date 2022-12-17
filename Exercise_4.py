# Exercise_4 : Merge Sort.

# Time Complexity: O(N log N), N = number of elements in array
# Space Complexity: O(N), since we use an additional array to store the sorted elements
# Successful Run on Leetcode: Yes (https://leetcode.com/problems/sort-an-array/)
# Challenges: None

# Python program for implementation of MergeSort 
def mergeSort(arr):
  # if the array has more than one element, split the array into two halves
  if len(arr) >= 2:
    # find the mid of the array
    mid = len(arr) // 2
    # split the array into two halves
    left = arr[:mid]
    right = arr[mid:]
    # recursively call mergeSort on the left and right halves of the array
    mergeSort(left)
    mergeSort(right)
    # merge the two halves of the array
    merge(arr, left, right)

def merge(arr, left, right):
  i = j = k = 0
  # while the left and right pointers are less than the length of the left and right halves of the array
  while i < len(left) and j < len(right):
    # if the left element is less than the right element, add the left element to the array and increment the left pointer
    if left[i] < right[j]:
      arr[k] = left[i]
      i += 1
    # if the right element is less than the left element, add the right element to the array and increment the right pointer
    else:
      arr[k] = right[j]
      j += 1
    # increment the array pointer
    k += 1
  # if the left pointer is less than the length of the left half of the array, add the remaining elements to the array
  while i < len(left):
    arr[k] = left[i]
    i += 1
    k += 1
  # if the right pointer is less than the length of the right half of the array, add the remaining elements to the array
  while j < len(right):
    arr[k] = right[j]
    j += 1
    k += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
