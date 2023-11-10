# Python program for implementation of MergeSort 
# Time complexity: O(n logn)
#Space Complexity: O(n)
def merge(left, right, arr):
    pl, pr, pa = 0,0,0
    while pl < len(left) and pr < len(right):
        if left[pl] <= right[pr]:
            arr[pa] = left[pl]
            pl += 1
        else:
            arr[pa] = right[pr]
            pr += 1
        pa += 1
    while pl < len(left):
        arr[pa] = left[pl]
        pl += 1
        pa += 1
    while pr < len(right):
        arr[pa] = right[pr]
        pr += 1
        pa += 1

def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]
    # print("Left", left)
    # print("right", right)
    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here


# driver code to test the above code
arr = [12, 11, 13, 5, 20, 7]
print ("Given array is", end="\n")
printList(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")
printList(arr)
