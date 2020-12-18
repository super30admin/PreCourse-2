# Python program for implementation of MergeSort 
def merge(arr, left, right):
    i = 0
    while left and right:
        if left[0] < right[0]:
            arr[i] = left.pop(0)
            i += 1
        else:
            arr[i] = right.pop(0)
            i += 1

    #Also taking care of the leftover elements
    while left:
        arr[i] = left.pop(0)
        i += 1
    while right:
        arr[i] = right.pop(0)
        i += 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)
        #print(arr)
  
# Code to print the list 
def printList(arr): 
    print(arr)
    return
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
