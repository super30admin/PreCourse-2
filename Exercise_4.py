# Python program for implementation of MergeSort

#Time Complexity: O(n log n)
#Space Complexity: O(n)

"""
Divide the array into two halves.

Recursively sort both halves.

Merge the sorted halves back into the original array.

"""
def mergeSort(arr):
  
  #write your code here

  if len(arr) > 1:
    mid = len(arr) // 2  # Find the middle
    left = arr[:mid]        # Left half
    right= arr[mid:]        # Right half

    # Recursively sort the two halves
    mergeSort(left)
    mergeSort(right)

    # Merge the sorted halves
    i = j = k = 0

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking for any leftover elements
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
    for i in arr:
        print(i, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
