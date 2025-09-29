# This is a simple Merge Sort implementation
# Time Complexity : O(n log n) 
# Space Complexity : O(n) due to temp arrays used for merging
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

def mergeSort(arr):
    # left and right define the current part of the array we are sorting
    left = 0
    right = len(arr) - 1

    # Only sort if there is more than one element
    if left < right:
        mid = (left + right) // 2  # find the middle index

        # Recursively sort the left half and right half
        l1 = mergeSort(arr[left:mid])
        l2 = mergeSort(arr[mid + 1:right])

        # lengths of left and right halves
        n1 = mid - left + 1
        n2 = right - mid

        # Create temporary arrays to hold the split parts
        L = [0] * n1
        R = [0] * n2

        # Copy data into temp arrays
        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        # Merge the temp arrays back into arr
        i = j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements of L[]
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy any remaining elements of R[]
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    return arr  # return the sorted array


  
# Code to print the list 
def printList(arr): 
    print(arr)
    

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
