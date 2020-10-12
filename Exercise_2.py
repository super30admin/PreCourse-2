# Python program for implementation of Quicksort Sort
"""
Time Complexity : O(nlogn)
Space Complexity : O(1)
Did this code successfully run on Leetcode : I don't know if this question is on Leetcode
                                            Please let me know in case it is
Any problem you faced while coding this : A bit. 
Your code here along with comments explaining your approach
"""

# give your explanation for the approach
"""
This is also a recursive approch where we are setting the pivot as the last value of the index
After each iteration, the pivot reaches it's actual place, ie, all smaller numbers are on its left
and all larger number are on its right.
"""


def partition(arr, low, high):
    pos = low-1
    pvt = arr[high]
    for x in range(low, high):
        if arr[x] < pvt:
            pos += 1
            arr[pos], arr[x] = arr[x], arr[pos]
    arr[pos+1], arr[high] = arr[high], arr[pos+1]
    return pos+1


def quickSort(arr, low, high):

    if low < high:
        index = partition(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)


    # Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
