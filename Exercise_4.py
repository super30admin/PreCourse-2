'''2 Approaches'''
'''
Algorithm (Recursive)
    merge(a, b):
        1. Initiate pointers i and j set them to 0. Also initialize an empty array result
        2. Iterate through both arrays. If either i or j pointer reach the
           end of their respective arrays go to step 5
        3. If element at a[i] less than equal to element at b[j] append a[i] to result, increment i by 1 and go to step 2
        4. If element at a[i] greater than element at b[j] append b[j] to result, increment j by 1 and go to step 2
        5. Concatinate result with remaining elements from a or b and return the new list

    mergeSort(arr):
        1. If length of arr is 1 simply return the array
        2. Else Split the arr into 2 halves and call mergesort recursively on each
        3. Call merge and pass the 2 halves and return the resulting array

mergeSort(arr):
    Space Complexity: space complexity of the merging process + size of recursion call stack = O(n) + O(logn) = O(n)
    Time Complexity: the merging time + the time to split the arrays = O(n) * O(logn) = O(n log n)
'''
# Python program for implementation of MergeSort recursive
print(f"MergeSort Recursive")


def merge(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result + a[i:] + b[j:]


def mergeSort(arr):
    # write your code here
    if len(arr) <= 1:
        return arr
    split1 = mergeSort(arr[:len(arr) // 2])
    split2 = mergeSort(arr[(len(arr) // 2):])
    return merge(split1, split2)


arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
arr = mergeSort(arr)
print("Sorted array is: ", end="\n")
print(arr)

# ######################Additional Test Cases##########################
# (1) Empty Array
assert mergeSort(
    []) == [], f"Expected[] as output but instead got {mergeSort([])}"

# (2) Single Element Array
op = mergeSort([1])
assert op == [1], f"Expected [1] as output but instead got {op}"

# (3) Minimal Unsorted Array Even
op = mergeSort([2, 1])
assert op == [1, 2], f"Expected [1,2] as output but instead got {op}"

# (4) Minimal Unsorted Array Odd
op = mergeSort([3, 2, 1])
assert op == [1, 2, 3], f"Expected [1,2,3] as output but instead got {op}"

# (5) Large Unsorted Array
arr = [10, 7, 8, 9, 1, 1, 1, 1, 5, 20, 10, 2, 4, 5, 6, 7, 100, 300]
sorted = [1, 1, 1, 1, 2, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 20, 100, 300]
op = mergeSort(arr)
assert op == sorted, f"Expected {sorted} as output but instead got {op}"

# #######################################################################

# Python program for implementation of MergeSort Iterative
'''
Algorithm (Iterative)
    mergeSort(arr):
        1.  Initialize offset i.e. partition size as 1.
        2.  Start iterating until offset is greater than the length of array then got to step 13
        3.  |    Initialize 2 pointers pointer_1 and pointer_2 to keep track
            |    of partition index we are currently visiting. 
        4.  |    Initialize 2 pointers partion_1_end and partion_2_end to keep track 
            |    of the end for current partitions
        5.  |    Initialize an empty result arr to store sorted results for current iteration
        6.  |    Start iterating until partion_2_end is less than current array as this will indicate 
            |    the arrays have been merged for current iteration
        7.  |    |   Start iterating until one of the pointers exceeds it's end then go to step 9
        8.  |    |   |     Compare pointer_1 and pointer_2 store lowest value in result and increment pointer for lower value
        9.  |    |   Insert all remainig elements in the result array 
        10. |    Increment the partitions and set pointers to travesere next batch then go to step 6
        11. Transfer the result back to the arr.
        12. Increment the offset and go back to step 2
        13. Return sorted arr
mergeSort(arr):
        Space Complexity: O(n) as we only require space to store merged array i.e. result
    Time Complexity: Outer loop (log n) + middle loop (log n) * Inner loop O(n) = O(2logn) * O(n) = O(n log n)
'''
print(f"Merge Sort Iterative")


def mergeSort(arr):
    offset = 1
    while offset < len(arr):
        pointer_1 = 0
        pointer_2 = offset + pointer_1
        partion_1_end = pointer_1 + offset
        partion_2_end = min(pointer_2 + offset, len(arr))
        result = []
        while partion_2_end <= len(arr):
            while pointer_1 < partion_1_end and pointer_2 < partion_2_end:
                if arr[pointer_1] <= arr[pointer_2]:
                    result.append(arr[pointer_1])
                    pointer_1 += 1
                else:
                    result.append(arr[pointer_2])
                    pointer_2 += 1
            if pointer_1 < partion_1_end:
                result = result + arr[pointer_1:partion_1_end]
            else:
                result = result + arr[pointer_2:partion_2_end]
            pointer_1 = partion_2_end
            pointer_2 = offset + pointer_1
            partion_1_end = pointer_1 + offset
            partion_2_end = pointer_2 + offset
            if partion_2_end > len(arr):
                result = result + arr[pointer_1:]
        arr = result
        offset += offset
    return arr


arr = [12, 11, 13, 5, 7, 6]
print("Given array is", end="\n")
print(arr)
arr = mergeSort(arr)
print("Sorted array is: ", end="\n")
print(arr)

# ######################Additional Test Cases##########################
# (1) Empty Array
arr = []
assert mergeSort(
    arr) == [], f"Expected[] as output but instead got {mergeSort(arr)}"

# (2) Single Element Array
arr = [1]
arr = mergeSort(arr)
assert arr == [1], f"Expected [1] as output but instead got {arr}"

# (3) Minimal Unsorted Array Even
arr = [2, 1]
arr = mergeSort(arr)
assert arr == [1, 2], f"Expected [1,2] as output but instead got {arr}"

# (4) Minimal Unsorted Array Odd
arr = [1, 2, 3]
arr = mergeSort(arr)
assert arr == [1, 2, 3], f"Expected [1,2,3] as output but instead got {arr}"

# (5) Large Unsorted Array
arr = [10, 7, 8, 9, 1, 1, 1, 1, 5, 20, 10, 2, 4, 5, 6, 7, 100, 300]
sorted = [1, 1, 1, 1, 2, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 20, 100, 300]
arr = mergeSort(arr)
assert arr == sorted, f"Expected {sorted} as output but instead got {arr}"

# #######################################################################
