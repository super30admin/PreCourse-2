# // Time Complexity : O(nlogn)
# // Space Complexity : O(2n) since we are creating arrays for each half
# // Did this code successfully run on Leetcode : NA
# // Any problem you faced while coding this : None
# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2                    # Divides the array into 2-halves until the length of array is less than 1
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return merge(left_half, right_half)        # Then the Merge function is called to merge both arrays

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):                # Compares the lowest among both arrays and appends it
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


# Code to print the list 
def printList(arr):
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
