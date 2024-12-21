# Python program for implementation of MergeSort 

# T: O(n log n), S: O(n)
def mergeSort(arr):
    # Base Case:
    if len(arr) <= 1:
        return arr

    # Recursive Step:
    # Split the array into halves
    mid = len(arr) // 2
    leftHalf = mergeSort(arr[:mid])
    rightHalf = mergeSort(arr[mid:])

    # Merge the sorted halves
    return merge(leftHalf, rightHalf)

def merge(left, right):
    sortedArray = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i += 1
        else:
            sortedArray.append(right[j])
            j += 1

    # Append remaining elements
    sortedArray.extend(left[i:])
    sortedArray.extend(right[j:])

    return sortedArray
  
# Code to print the list 
def printList(arr):
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sortedArr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(sortedArr) 
