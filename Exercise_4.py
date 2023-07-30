# Python program for implementation of MergeSort
from math import floor
"""
TC->0(nlogn)
"""

def merge(left, right):
    # list1 = []
    # list2 = []
    res = []
    # for i in range(0,len(left)):
    #     list1.append(left[i])
    # for j in range(0,len(right)):
    #     list2.append(right[j])

    left_index = 0
    right_index = 0
    while(left_index<len(left) and right_index<len(right)):
        if left[left_index]<right[right_index]:
            res.append(left[left_index])
            left_index = left_index+1
        else:
            res.append(right[right_index])
            right_index = right_index+1



    res.extend(left[left_index:])
    res.extend(right[right_index:])
    return res


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    low = 0
    high = len(arr) - 1
    middle = floor((low + high) / 2)
    left = mergeSort(arr[:middle+1])
    print("mergesort of ",arr[:middle+1])
    right = mergeSort(arr[middle+1:])
    print("mergesort of ", arr[middle + 1:])
    y =merge(left, right)
    print("merge of ",left,right)
    return y


# Code to print the list
def printList(arr):
    print(arr)
    # write your code here


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    y = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(y)
