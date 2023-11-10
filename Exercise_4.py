# Python program for implementation of MergeSort
# timecomplexity: O(nlogn), space complexity: O(n)
#No issues faced while solving
def mergeSort(arr):
    #base condition
    if len(arr) < 2:
        return arr
    #find the mid point
    mid = len(arr) // 2

    #divide until you can't divide the array anymore using recursion
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left, right):
    #If either one of the left or right halves are not existant return the latter
    if not len(left) or not len(right):
        return left or right

    res = []
    a, b = 0, 0

    #Till the partitions combined are of the same size of initial unsorted array
    while len(res) < len(left) + len(right):
        #if left array index lesser than right append it to the result and vice versa
        if left[a] < right[b]:
            res.append(left[a])
            a += 1
        else:
            res.append(right[b])
            b += 1
        #If one onf the halves have been completely sorted can be extended with result
        if a == len(left) or b == len(right):
            res.extend(left[a:] or right[b:])
            break

    return res


# Code to print the list
def printList(arr):
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(mergeSort(arr))