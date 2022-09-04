# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge_two_sorted_lists(left, right)

# write your code here
def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list
# Code to print the list
def printList(arr):
    print(arr)

# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    print("Sorted array is: ", end="\n")
    printList(mergeSort(arr))