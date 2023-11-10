# Time Complexity : log(n*log n)
# Space Complexity : O(n)

# Python program for implementation of MergeSort
def mergeSort(arr):

    if len(arr) > 1:
        i = j = k = 0

        # find the midpoint of the array
        right = len(arr) // 2

        # divide the array into two halves
        left_array = arr[:right]
        right_array = arr[right:]

        # Applying merge sort on two arrays until the array length is 1
        mergeSort(left_array)
        mergeSort(right_array)

        # merging two arrays by comparing the elements from each array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        # check if there are any remaining elements in each array and then append them to the arr
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

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
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
