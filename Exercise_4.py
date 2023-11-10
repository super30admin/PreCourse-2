# Python program for implementation of MergeSort 

# Time Complexity : O(n^2)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_lst = arr[mid:]
        mergeSort(left_list)
        mergeSort(right_lst)
        i = 0
        j = 0
        k = 0
        if left_list[i] < right_lst[j]:
            arr[k] = left_list[i]
        else:
            arr[k] = right_lst[j]
            while i<len(left_list) and j<len(right_lst):
                if left_list[i] < right_lst[j]:
                    arr[k] = left_list[i]
                    i = i+1
                    k = k+1
                else:
                    arr[k] = right_lst[j]
                    j = j+1
                    k = k+1
            while i<len(left_list):
                arr[k] = left_list[i]
                i = i+1
                k = k+1
            while j<len(right_lst):
                arr[k] = right_lst[j]
                j = j+1
    return arr
def printList(arr):
    return arr

# driver code to test the above code 
arr = [12, 11, 13, 5, 6, 7]  
print ("Given array is", end="\n")  
print(printList(arr))
mergeSort(arr) 
print("Sorted array is: ", end="\n") 
print(printList(arr)) 
