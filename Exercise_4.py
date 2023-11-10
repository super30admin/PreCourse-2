# Python program for implementation of MergeSort
# TC: O(n log(n))
# SC: O(N) or O(N log(N)) because we're temporary creating subarrays.

from types import resolve_bases

# split the array until there's only one element left
# compare the left most element of the both arr1 and arr2 
# push the smaller one into the main array 
# there can be 3 scenarios after every push, 
# both arr1 and arr2 are done
# only arr2 is done, there are still some elements remaining in the arr1
# only arr1 is done, arr2 remaining
def mergeSort(arr):
    # if arr size is 1 then it is already sorted so skip those
    if len(arr) > 1:
        arr1, arr2 = arr[: len(arr) // 2], arr[len(arr) // 2 :]
        mergeSort(arr1)
        mergeSort(arr2)
        n = len(arr)
        insertAt = len(arr) - 1
        for i in range(n):
            if len(arr1) != 0 and len(arr2) != 0:
                if arr1[len(arr1) - 1] > arr2[len(arr2) - 1]:
                    arr[insertAt]= arr1.pop()
                    insertAt -= 1 
                else:
                    arr[insertAt]=arr2.pop()
                    insertAt -= 1
            elif len(arr1) != 0 and len(arr2) == 0:
                arr[insertAt] = arr1.pop()
                insertAt -= 1
            elif len(arr2) != 0 and len(arr1) == 0:
                arr[insertAt] = arr2.pop()
                insertAt -= 1
        return arr
            # if n == i+1 & 


# Code to print the list
# def printList(arr):

# write your code here

# driver code to test the above code
if __name__ == "__main__":
    arr = [35, 2, 234, 43, 12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    # printList(arr)
    print(arr)
    
    print("Sorted array is: ", end="\n")
    print(mergeSort(arr))
    # printList(arr)
