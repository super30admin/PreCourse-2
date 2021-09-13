# Python program for implementation of MergeSort

def merge(arr, arr1, arr2):
    
    p_arr = 0
    p_arr1 = 0
    p_arr2 = 0
    
    while (p_arr1 < len(arr1)) and (p_arr2 < len(arr2)):
        
        if arr1[p_arr1] <= arr2[p_arr2]:
            arr[p_arr] = arr1[p_arr1]
            p_arr1 += 1
        else:
            arr[p_arr] = arr2[p_arr2]
            p_arr2 += 1
        
        p_arr += 1
        
    while (p_arr1 < len(arr1)):
        arr[p_arr] = arr1[p_arr1]
        p_arr += 1
        p_arr1 += 1
        
    while (p_arr2 < len(arr2)):
        arr[p_arr] = arr2[p_arr2]
        p_arr += 1
        p_arr2 += 1
        

    
def mergeSort(arr):
    
    arr_len = len(arr)
    
    if (arr_len == 0) or (arr_len == 1):
        return arr
    
    mid = arr_len//2
    
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    
    mergeSort(arr1)
    mergeSort(arr2)
    
    merge(arr, arr1, arr2)
    
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)


# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)