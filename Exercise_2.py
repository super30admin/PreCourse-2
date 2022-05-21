""""// Time Complexity : 42ms
// Space Complexity : nlog(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach"""


# Python program for implementation of Quicksort Sort


def partition(arr, low, high):
    i=low
    j=high-1
    pivot=arr[high]
    while i<j:
        while i<high and arr[i]<pivot:
            i=i+1
        while j>low and arr[j]>=pivot:
            j=j-1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]# Swapping element at i with element at j
    if arr[i]>pivot:
        arr[i], arr[high]= arr[high], arr[i]
    return i # Return the position from where partition is done





# Function to do Quick sort - recursion
def quickSort(arr, low, high):
    if low<high:
        pos=partition(arr, low, high)
        quickSort(arr, low, pos-1)
        quickSort(arr, pos+1, high)




# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
"""print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),"""