# Python program for implementation of MergeSort 
#TimeComplexity: O(n log n)
#SpaceComplexity: O(n)    

def mergeSort(arr):
    
    #if ther array has more than one element
    if len(arr)>1:
        #get the middle index and divide the array into two and apply merge sort to both
        mid = len(arr) // 2
        arr_1 = arr[:mid]
        arr_2 = arr[mid:]
        mergeSort(arr_1)
        mergeSort(arr_2)
        
        #merge
        ind_1 = 0
        ind_2 = 0
        ind_arr = 0
        
        #for both array sort and merge elements
        while ind_1 < len(arr_1) and ind_2 < len(arr_2):
            if arr_1[ind_1] < arr_2[ind_2]:
                arr[ind_arr] = arr_1[ind_1]
                ind_1 += 1
            else:
                arr[ind_arr] = arr_2[ind_2]
                ind_2 += 1
            ind_arr += 1
        
        #if any elements are left to be put in arr from arr_1
        while ind_1 < len(arr_1):
            arr[ind_arr] = arr_1[ind_1]
            ind_arr += 1
            ind_1 += 1
        #if any elements are left to be put in arr from arr_2    
        while ind_2 < len(arr_2):
            arr[ind_arr] = arr_2[ind_2]
            ind_arr += 1
            ind_2 += 1
  
# Code to print the list 
def printList(arr): 
    
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
