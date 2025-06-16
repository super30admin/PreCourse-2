# Time Complexity: O(n log n) in all cases (Best, Average, Worst)
# Space Complexity: O(n) due to auxiliary arrays used for merging

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        L = arr[:mid]        # Dividing the array into two halves
        R = arr[mid:]

        mergeSort(L)         # Sorting the first half
        mergeSort(R)         # Sorting the second half

        # Merging the two halves
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left in L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Checking if any element was left in R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end=" ") 
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
