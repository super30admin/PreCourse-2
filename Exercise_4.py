""""// Time Complexity : 64ms
// Space Complexity : nlog(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach"""


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Sorting the first half
        mergeSort(left_arr)

        # Sorting the second half
        mergeSort(right_arr)

        i = 0 #left arr index
        j = 0 #right arr index
        k = 0 #merged arr index

        # Copy data to temp arrays L[] and R[]
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            # Checking if any element was left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    # Code to print the list


# write your code here

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    #print(arr)
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    #print(arr)
    printList(arr)