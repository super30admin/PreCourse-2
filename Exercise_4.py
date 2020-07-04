# Python program for implementation of MergeSort 
def mergeSort(arr):

    #write your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergeSort(left_arr)
        mergeSort(right_arr)

        left_ind, right_ind, main_ind = 0, 0, 0
        while left_ind < len(left_arr) and right_ind < len(right_arr):
            if left_arr[left_ind] <= right_arr[right_ind]:
                arr[main_ind] = left_arr[left_ind]
                left_ind += 1

            elif left_arr[left_ind] > right_arr[right_ind]:
                arr[main_ind] = right_arr[right_ind]
                right_ind += 1

            main_ind += 1

        while left_ind < len(left_arr):
            arr[main_ind] = left_arr[left_ind]
            main_ind += 1
            left_ind += 1

        while right_ind < len(right_arr):
            arr[main_ind] = right_arr[right_ind]
            right_ind += 1
            main_ind += 1



  
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
