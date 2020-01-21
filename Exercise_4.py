# Python program for implementation of MergeSort 

def merge(a: list, b: list) -> list:
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    result = []
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len_a:
        result.append(a[i])
        i += 1
    while j < len_b:
        result.append(b[j])
        j += 1
    return result


def mergeSort(arr: list) -> list:
    """
    Time complexity - O(nlogn)
    We are dividing the array in two halves logn times and at each level
    we need to traverse the whole array during merging
    Space Complexity -
        If we do not clear the extra memory for left and right array O(nlogn)
        If we clear the extra memory: O(2n) or O(n) because at any time at
        level 1 (n/2), level 2 (n/4), level 3 (n/8). n(1/2+1/4+1/8)= n(2) = 2n.
        which can be written as O(n)
        Stable algorithm, Recusrive, Divide and conquer strategy
    """
    # base case
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])
    return merge(left_half, right_half)


def printList(arr: list) -> None:
    for i in arr:
        print(i, end=' ')


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("\nSorted array is: ", end="\n")
    printList(arr)
