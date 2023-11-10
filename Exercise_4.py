# Python program for implementation of MergeSort
# In mergesort we divide the input array into two halves, call mergesort for the two halves, and then merge the two sorted halves and we do this by recursion
#Time Complexity : O(NLogN)
#Space Complexity : O(N)
#Any problem you faced while coding this : No
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        l = arr[:mid]

        # into 2 halves
        r = arr[mid:]

        # Sorting the first half
        mergeSort(l)

        # Sorting the second half
        mergeSort(r)

        i = j = k = 0

        # Copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print("%d" % arr[i],end=" ")

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
