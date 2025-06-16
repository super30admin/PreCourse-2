#Time Complexity : O(n log n)
#Space Complexity : O(n)

#Code for merge
def merge(arr, low, mid, high):
    ArrB = []
    i = low
    j = mid+1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            ArrB.append(arr[i])
            i += 1
        else:
            ArrB.append(arr[j])
            j += 1
    while i <= mid:
        ArrB.append(arr[i])
        i += 1
    while j <= high:
        ArrB.append(arr[j])
        j += 1
    for k in range(len(ArrB)):
        arr[low + k] = ArrB[k]

# Python program for implementation of MergeSort 
def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)
  
# Code to print the list 
def printList(arr):
    print(arr)
      
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
