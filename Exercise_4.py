# Time complexity: O(nlog n)
# Space complexity: O(n)

# Idea is to split the array into two halves sort the two halves while merging them together. Divide and conquer strategy
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    left_idx, right_idx = 0, 0
    result = []
    # as long as the indices are within limits, add the minimum elements to the result array and advance respective indices
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    # if there are any elements left in either left or right array, add the to the result
    if left_idx < len(left):
        result += left[left_idx:]
    if right_idx < len(right):
        result += right[right_idx:]
    return result

# Code to print the list


def printList(arr):
    print(arr)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
