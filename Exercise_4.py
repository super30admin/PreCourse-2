"""
Time Complexity:
merge: O(n) where n is the total length of left and right arrays
mergeSort: O(n log n) as we divide the array in half each time (log n) and merge takes O(n)

Worst Case: O(n log n) - Merge sort maintains consistent performance regardless of input order
Best Case: O(n log n) - Even with sorted input, we still need to perform all divisions and merges

Space Complexity:
merge: O(n) for the result array
mergeSort: O(n) for the recursive call stack and temporary arrays
"""

# Python program for implementation of MergeSort 
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

# Test the implementation
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
sorted_arr = mergeSort(arr)
print("Sorted array:", sorted_arr)

#write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
  
# driver code to test the above code 
    if __name__ == '__main__': 
        arr = [12, 11, 13, 5, 6, 7]  
        print ("Given array is", end="\n")  
        printList(arr) 
        sorted_arr = mergeSort(arr)
        print("Sorted array is: ", end="\n") 
        printList(sorted_arr) 
