# Time Complexity : Best and Average case: O(N*LogN) when partition happens approx from the middle that is position of pivot 
# element is mostly near the middle of the array.
# Worst Case: O(N**2) = O(N^2): When array is already sorted in Ascending or Descending Order. In this case partitions are very
# imbalanced. The number of partitions would be O(N). Also our partition function is already O(N). So overall Time complexity would be O(N**2)
# Space Complexity : O(1) extra space. O(N) auxiliary recursive stack space
# Did this code successfully run on Leetcode : Could not find on Leetcode
# Any problem you faced while coding this : I went through Algorithm explanation and psuedo code. Then I was able to implement it.
# There are many ways to implement the partition function. Can you please guide which one is better?


# Your code here along with comments explaining your approach
# Here I have written the code for Sorting in Ascending Order.
# It is based on choosing pivot and then partitioning the array
# Here I am taking pivot as the last element that is arr[high] for the range of [low, high]
# Then we place the pivot on its correct place by bringing all smaller and equal to pivot elements on the Left Portion and larger than pivot 
# as the right portion
# Then we recursively apply the pivot and partition logic on the Left portion and the Right Portion
# If we want to sort the array in descending order, I believe with minor tweak in the partition function "if(arr[j] >= pivot)" , 
# would help us to do it. It would bring the larger and equal to pivot elements to the left

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    # used to bring the smaller or equal to pivot elements to the left portion
    idx = low - 1

    for j in range(low, high):
        if(arr[j] <= pivot):
            idx += 1
            arr[j], arr[idx] = arr[idx], arr[j]

    # bring the pivot to its correct place
    idx += 1
    arr[high], arr[idx] = arr[idx], arr[high]
    return idx

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if(low < high):
        pIndex = partition(arr,low,high)
        quickSort(arr, low, pIndex - 1)
        quickSort(arr, pIndex + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [6, 5, 4, 3, 2, 1]
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [7, 8, 9, 10, 11, 12, 13]
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = [7, 7, 7, 7, 7, 7]
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")

print()
arr = []
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is:") 
for i in range(n): 
    print("%d " %arr[i], end="")
  
 
