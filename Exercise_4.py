# Python program for implementation of MergeSort
# Time Complexity : O(N LOGN)
# Space Complexity : O(N)

def merge(arr, low, midPosition, high):
    temp = []
    left = low
    right = midPosition+1

    while (left <= midPosition and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left = left+1
        else:
            temp.append(arr[right])
            right = right+1

    while (left <= midPosition):
        temp.append(arr[left])
        left = left+1

    while (right <= high):
        temp.append(arr[right])
        right = right+1

    for i in range(low, high+1):
        arr[i] = temp[i-low]


def mS(arr, low, high):

    if low == high:
        return
    else:
        midPosition = (low+high)//2
        mS(arr, low, midPosition)
        mS(arr, midPosition+1, high)
        merge(arr, low, midPosition, high)


def mergeSort(arr):

    low = 0
    high = len(arr)-1
    mS(arr, low, high)

  # write your code here

# Code to print the list


def printList(arr):

    # write your code here
    print(arr)


    # driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
