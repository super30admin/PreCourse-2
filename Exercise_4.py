# Python program for implementation of MergeSort 
def mergeSort(arr):
    if (len(arr) > 1):
        mid_index = len(arr) // 2

        left_array = arr[:mid_index]
        right_array = arr[mid_index:]

        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0
        while (i < len(left_array) and j < len(right_array)):
            if (left_array[i] < right_array[j]):
                arr[k] = left_array[i]
                i = i + 1
            else:
                arr[k] = right_array[j]
                j = j + 1
            k = k + 1

        while (i < len(left_array)):
            arr[k] = left_array[i]
            i = i + 1
            k = k + 1

        while (j < len(right_array)):
            arr[k] = right_array[j]
            j = j + 1
            k = k + 1


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

