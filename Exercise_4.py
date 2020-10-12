# Python program for implementation of MergeSort
"""
Time Complexity : O(nlogn)
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : Not much. I have some issues in understanding recursion properly
Your code here along with comments explaining your approach
"""


def mergeSort(arr):
    """
    This is a recursive algorithm. The function continously divides the array into half untill it reaches
    one single element. Then it backtracks and starts sorting, one subarray at a time.
    """
    length = len(arr)
    if length > 1:
        mid = length//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        x = y = z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x += 1
            else:
                arr[z] = right[y]
                y += 1
            z += 1
        while x < len(left):
            arr[z] = left[x]
            x += 1
            z += 1
        while y < len(right):
            arr[z] = right[y]
            y += 1
            z += 1


# Code to print the list
def printList(arr):
    for a in arr:
        print(a)


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
