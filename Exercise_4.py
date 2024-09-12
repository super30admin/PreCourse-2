# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)>1:
        mid_point= len(arr)//2
        left_arr=arr[:mid_point]
        right_arr=arr[mid_point:]
        mergeSort(left_arr)
        mergeSort(right_arr)

#merging_back_sorted_subarrays
        i=j=k=0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
#checking_for_remaining_elements_in_subarray
        while i<len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            j+=1
            k+=1
# Code to print the list 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

# driver code to test the above code
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
