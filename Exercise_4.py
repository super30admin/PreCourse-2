# Python program for implementation of MergeSort
# Time Complexity : O(nLogn)
#  Space Complexity : 0(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :


def mergeSort(arr):
    if len(arr) > 1:

        #Get mid of the list
        mid = len(arr) // 2

        # Creat left and right partition using mid
        left = arr[:mid]
        right = arr[mid:]
        # Sorting the first half
        mergeSort(left)

        # Sorting the second half
        mergeSort(right)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
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
    for i in range(len(arr)):
        print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ")
    printList(arr) 
