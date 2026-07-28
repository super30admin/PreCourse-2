# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Did this code successfully run on LeetCode: Not directly applicable because LeetCode uses a different function format

# Any problem you faced while coding this: The main challenge was correctly merging the two sorted halves and copying any remaining elements

# Approach:
# 1. Divide the array into two halves
# 2. Recursively sort the left half
# 3. Recursively sort the right half
# 4. Merge the two sorted halves back into the original array

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

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
  
  
# Code to print the list 
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
