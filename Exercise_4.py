# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  #Base Case, if input array has only 1 element then return
    if len(arr) <= 1:
        return arr

    #Divide the array into two parts
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    #Divide the array until we get the one element
    arr1 = mergeSort(arr1) 
    arr2 = mergeSort(arr2)

    return merge_two_sort_arrays(arr1, arr2)

def merge_two_sort_arrays(arr1, arr2):
    temp = []
    pointer1 = 0
    pointer2 = 0 
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            temp.append(arr1[pointer1])
            pointer1 = pointer1 + 1
        else:
            temp.append(arr2[pointer2])
            pointer2 = pointer2 + 1

    if pointer1 < pointer2:
        while pointer1 != len(arr1):
            temp.append(arr1[pointer1])
            pointer1 = pointer1 + 1
    else:
        while pointer2 != len(arr2):
            temp.append(arr2[pointer2])
            pointer2 = pointer2 + 1 
    
    return temp

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print(f"Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
