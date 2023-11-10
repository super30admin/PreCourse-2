# Exercise_2 : Recursive QuickSort

# Average-Case Time Complexity: O(N log N), N = number of elements in array
# Worst-Case Time Complexity: O(N^2), N = number of elements in array
# Space Complexity: O(N), N = number of elements in array (Partition is unbalanced, and one recursive call is made at each level. The depth of the tree is N, so recursion call stack size is O(N))
# Successful Run on Leetcode: Yes (https://leetcode.com/problems/sort-an-array/)
# Challenges: None

def partition(arr,low,high):
  # partition the array using the last element as the pivot
  pivot = arr[high]
  # set the index of the smaller element to the left of the pivot
  i = low - 1
  # iterate through the array
  for j in range(low, high):
    # if the current element is smaller than the pivot
    if arr[j] < pivot:
      # increment the index of the smaller element
      i += 1
      # swap the current element with the element at the index of the smaller element
      arr[i], arr[j] = arr[j], arr[i]
  # swap the element at the index of the smaller element with the pivot
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  # return the index of the pivot
  return i + 1
  

def quickSort(arr,low,high): 
    if low < high:
        # p is the partitioning index
        # arr[p] is placed in the correct position
        p = partition(arr,low,high)
        # sort the elements before and after the partition
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print(arr[i])
  
 
