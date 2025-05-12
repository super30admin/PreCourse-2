# Python program for implementation of MergeSort 

# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Couldn't find this problem on Leetcode
# Any problem you faced while coding this: I need to practice more on this, it's a bit confusing

def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves
        left = arr[:mid]
        right = arr[mid:]
        
        # Sorting the first half
        mergeSort(left)
        
        # Sorting the second half
        mergeSort(right)
        
        # Merge the sorted halves
        i = j = k = 0 # Initialize pointers for left, right, and merged arrays
        
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
