# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Any problem you faced while coding this : No
# Python program for implementation of MergeSort. We find the mid as m, split the array into left and right and recursively call mergeSort on left and right.
# Then we iterate through left, right, compare elements to add to the array
def mergeSort(arr):
    if len(arr) > 1:

        m = len(arr)//2

        leftArr = arr[:m]
        rightArr = arr[m:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        leftIter = rightIter = arrIter = 0

        while leftIter < len(leftArr) and rightIter < len(rightArr):
            if leftArr[leftIter] < rightArr[rightIter]:
                arr[arrIter] = leftArr[leftIter]
                leftIter += 1
            else:
                arr[arrIter] = rightArr[rightIter]
                rightIter += 1
            arrIter += 1

        # Checking if any element left in the left array
        while leftIter < len(leftArr):
            arr[arrIter] = leftArr[leftIter]
            leftIter += 1
            arrIter += 1

        # Checking if any element left in the right array
        while rightIter < len(rightArr):
            arr[arrIter] = rightArr[rightIter]
            rightIter += 1
            arrIter += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])
    #write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
