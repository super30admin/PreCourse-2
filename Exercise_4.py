"""
Time Complexity : O( n*log(n) )
Space Complexity : O(n)
"""



def MergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        MergeSort(left)
        MergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def PrintArr(arr):
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [23,13,4,7,9,11]
    print("Original Array", end="\n")
    PrintArr(arr)
    MergeSort(arr)
    print("Sorted Array", end="\n")
    PrintArr(arr)
