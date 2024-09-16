# Python code to implement iterative Binary  
# Search. 

# It returns location of x in given array arr
# if present, else returns -1
def binarySearch_withoutmid(arrayString, leftPointer, rightPointer, target):
    arrayString = sorted(arrayString)
    print(arrayString)

    while (leftPointer <= rightPointer):

        if arrayString[leftPointer] == target:
            return leftPointer
        if arrayString[rightPointer] == target:
            return rightPointer
        if arrayString[leftPointer] < target and arrayString[rightPointer] > target:
            leftPointer += 1
            rightPointer -= 1
        elif arrayString[leftPointer] < target and arrayString[rightPointer] < target:
            leftPointer += 1
        elif arrayString[leftPointer] > target and arrayString[rightPointer] > target:
            return -1

    return -1


def binarySearch_withmid(arrayString, leftPointer, rightPointer, target):
    # arrayString= sorted(arrayString)
    isasending = arrayString[leftPointer] < arrayString[rightPointer]
    while (leftPointer <= rightPointer):
        mid = leftPointer + (rightPointer - leftPointer) // 2
        print(mid)
        if arrayString[mid] == target:
            return mid

        if isasending:
            if arrayString[mid] > target:
                rightPointer = mid - 1
            else:
                leftPointer = mid + 1
        else:
            if arrayString[mid] > target:
                leftPointer = mid + 1
            else:
                rightPointer = mid - 1

    return -1


# write your code here


# Test array
arr = [1, 2, 3, 4, 90, 4]
x = 90

# Function call
# result = binarySearch_withoutmid(arr, 0, len(arr)-1, x)
result = binarySearch_withmid(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")
