# Python program for implementation of MergeSort 
def merge(arr, left_index, right_index):

    # O(n) Time Complexity | O(n) Space Complexity

    new_arr = []
    curr_index = 0

    left_ptr = left_index
    right_ptr = int(right_index / 2) + 1

    left_max_index = right_ptr - 1
    right_max_index = right_index

    while (True):           # 4 conditions to be checked and if none of the 4 satisfy, break the loop
        if (left_ptr <= left_max_index and right_ptr <= right_max_index) and (arr[left_ptr] < arr[right_ptr]):
            new_arr.append(arr[left_ptr])
            left_ptr += 1
            curr_index += 1
            continue
        if (left_ptr <= left_max_index and right_ptr <= right_max_index) and (arr[left_ptr] >= arr[right_ptr]):
            new_arr.append(arr[right_ptr])
            right_ptr += 1
            curr_index += 1
            continue
        if (left_ptr > left_max_index and right_ptr <= right_max_index):
            new_arr.append(arr[right_ptr])
            right_ptr += 1
            curr_index += 1
            continue
        if (left_ptr <= left_max_index and right_ptr > right_max_index):
            new_arr.append(arr[left_ptr])
            left_ptr += 1
            curr_index += 1
            continue
        break

    for i in range(len(new_arr)):
        arr[left_index + i] = new_arr[i]


def mergeSortHelper(arr, left_index, right_index):

    # O (n.logn) Time Complexity | O(n) Space Complexity
    if (left_index >= right_index):
        return
    mid_index = int((right_index + left_index)/ 2)
    mergeSortHelper(arr, left_index, mid_index)     # recursive merge sort on first half
    mergeSortHelper(arr, mid_index + 1, right_index)    # recursive merge sort on second half
    merge(arr, left_index, right_index)             # merge the two halves

def mergeSort(arr):
  
  #write your code here
    mergeSortHelper(arr, 0, len(arr) - 1)
  
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
