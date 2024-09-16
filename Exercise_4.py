# Python program for implementation of MergeSort
ans = []

def merge(arr, left, mid, right):
    global ans
    l_ptr = left
    r_ptr = mid + 1
    ptr = 0

    while l_ptr <= mid and r_ptr <= right:
        if arr[l_ptr] <= arr[r_ptr]:
            ans[ptr] = arr[l_ptr]
            l_ptr += 1
        else:
            ans[ptr] = arr[r_ptr]
            r_ptr += 1
        ptr += 1

    while l_ptr <= mid:
        ans[ptr] = arr[l_ptr]
        l_ptr += 1
        ptr += 1

    while r_ptr <= right:
        ans[ptr] = arr[r_ptr]
        r_ptr += 1
        ptr += 1

    for i in range(ptr):
        arr[left + i] = ans[i]

def merge_sort(arr, left, right):
    if left >= right:
        return
    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

def mergeSort(arr):
    global ans
    ans = [0] * len(arr)
    merge_sort(arr, 0, len(arr) - 1)

# Code to print the list
def printList(arr):
    for e in arr:
        print(e, end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 6, 5]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
