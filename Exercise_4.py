# Python program for implementation of MergeSort 
#Time Complexity O(nlogn)
#Space Complexity O(n)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # Find the middle
        L = arr[:mid]         # Left half
        R = arr[mid:]         # Right half

        # Recursively sort both halves
        mergeSort(L)
        mergeSort(R)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy any remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Function to print array
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
