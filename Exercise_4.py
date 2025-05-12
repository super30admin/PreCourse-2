
# Time Complexity: O(n log n) – because we divide the array and merge it back recursively.
# Space Complexity: O(n) – we use additional space for left and right halves.

#Any problem you faced while coding this?: 
# The merge part was a bit tricky to get right at first. 
#Took a couple of tries to understand how the pointers i, j, and k should move.

# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle point
        left = arr[:mid]     # Divide the array elements into 2 halves
        right = arr[mid:]

        mergeSort(left)      # Sort the first half
        mergeSort(right)     # Sort the second half

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left in left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was left in right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
    for i in arr:
        print(i, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is:") 
    printList(arr)

