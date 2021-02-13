# Python program for implementation of MergeSort
# Time Complexity : O(nlogn)
# Space Complexity  : O (n)
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left_list = arr[:mid]
        right_list = arr[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j< len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i += 1
                k += 1
            else:
                arr[k] = right_list[j]
                j += 1
                k += 1
        while i< len(left_list):
            arr[k] = left_list[i]
            i += 1
            k += 1
        while j< len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1
    else:
        return arr

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    for i in range (len(arr)):
        print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
