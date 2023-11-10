# Python program for implementation of MergeSort
#Time Complexity = O(nlogn)
#Space Complexity = O(1)
def merge_two_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i=j=k=0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)

    mergeSort(right)
    merge_two_list(left,right,arr)

  #write your code here

# Code to print the list
def printList(arr):
    print(arr)
    #write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is")
    printList(arr)
    x = mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)
