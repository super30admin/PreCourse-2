# Time Complexity : O(n log n) in all cases
# Space Complexity : O(n) due to temporary arrays
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : No, but remember to handle merge step carefully

# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort both halves
        mergeSort(left_half)
        mergeSort(right_half)
        
        # Merge the sorted halves
        # i = left index
        # j = right index
        i = j = curr = 0
        
        # Copy data from temp arrays back to main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[curr] = left_half[i]
                i += 1
            else:
                arr[curr] = right_half[j]
                j += 1
            curr += 1
        
        # Copy remaining elements of left_half
        while i < len(left_half):
            arr[curr] = left_half[i]
            i += 1
            curr += 1
        
        # Copy remaining elements of right_half
        while j < len(right_half):
            arr[curr] = right_half[j]
            j += 1
            curr += 1

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
