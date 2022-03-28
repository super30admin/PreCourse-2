# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Python program for implementation of MergeSort
def mergeSort(arr):
    if(len(arr) > 1):
        # checking the middle element of the array
        midValue = int(len(arr)/2)
        # assigning first and second halves separately
        leftValues = arr[0:midValue]
        rightValues = arr[midValue:]
        # sorting the both halves among themselves
        mergeSort(leftValues)
        mergeSort(rightValues)
        # initializing index for each array
        i = j = k = 0
        # checking the larger values and placing them is correct positions for both the arrays
        while(i < len(leftValues) and j < len(rightValues)):
            if(leftValues[i] < rightValues[j]):
                arr[k] = leftValues[i]
                i = i+1
            else:
                arr[k] = rightValues[j]
                j = j+1
            k = k+1
        # checking all the remaining elements
        while(i < len(leftValues)):
            arr[k] = leftValues[i]
            i = i+1
            k = k+1
        while(j < len(rightValues)):
            arr[k] = rightValues[j]
            j = j+1
            k = k+1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    print()

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
