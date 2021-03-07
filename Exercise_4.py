# Python program for implementation of MergeSort 
def merge(arr, l, m, h):
    left = arr[l:m + 1]
    right = arr[m + 1: h + 1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(l, h+1):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def mergeSort(arr, l, h):
    #write your code here
    if l < h:
        mid = (l + h) // 2
        mergeSort(arr, l , mid)
        mergeSort(arr, mid + 1 ,h)
        merge(arr, l, mid, h)
  
# Code to print the list 
def printList(arr): 
    #write your code here
    for elem in arr:
        print(elem, end = " ")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7, 1]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr) - 1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
