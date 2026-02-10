# Python program for implementation of MergeSort 

# Merge sort is also a devide and conqure approach. But in this the arrays are sorted during merging
# Basically we keep on deviding the arrays in half untill thhe last 2 elements are left 1 in left array 
# and 2nd in right array. Then from that we start rebuilding the array by comparing the values in 
# both subarray and assigning to the actual array
def mergeSort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1

    if left < right:
        mid = (left+right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)

        merge(arr, left, mid, right)

    
def merge(arr, left, mid, right):
    arr1 = []
    arr2 = []

    for i in range(left, mid+1):
        arr1.append(arr[i])

    for j in range(mid+1, right+1):
        arr2.append(arr[j])

    i = 0
    j = 0
    k=left
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k] = arr2[j]
            j+=1
        k+=1
    
    if i != len(arr1):
        while i < len(arr1):
            arr[k] = arr1[i]
            i+=1
            k+=1

    if j != len(arr2):
        while j < len(arr2):
            arr[k] = arr2[j]
            j+=1
            k+=1
    return
      

    
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
