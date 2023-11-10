# Python program for implementation of MergeSort
# Time complexity = O(nlogn)
# Space complexity = O(n)

def mergeSort(arr):

    n = len(arr)
    if (n > 1): # applying merge sort only if arr size is greater than 1

        mid = len(arr) // 2

        leftlist = arr[:mid] # forming 2 sub-lists
        rightlist = arr[mid:]

        mergeSort(leftlist) #recursively calling merge sort - till we reach single element
        mergeSort(rightlist)

        i,j,k = 0,0,0 # here i = pointer for leftlist, j = pointer for rightlist and k = pointer for main arr list

        # Merging Logic
        while i < len(leftlist) and j < len(rightlist): #comparing val in left and right list
            if leftlist[i] <= rightlist[j]: # smallest among them will replace val in main arr list
                arr[k] = leftlist[i]
                i += 1
            else:
                # rightlist[j] <= leftlist[i]:
                arr[k] = rightlist[j]
                j += 1
            k += 1
        # when one of the either list gets exhausted, just replace main arr list with remaining values
        while i < len(leftlist):
            arr[k] = leftlist[i]
            i += 1
            k += 1

        while j < len(leftlist):
            arr[k] = rightlist[j]
            j += 1
            k += 1





# Code to print the list
def printList(arr):

    n = len(arr)
    for i in range(0,n):
        print("%d" % arr[i]),


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    # print("Given array is", end="\n")
    # printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

  
 
