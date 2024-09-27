# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
    if not arr:
        return

    if len(arr) > 1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_list= arr[mid:]

        mergeSort(left_list)
        mergeSort(right_list)

        i,j,k=0,0,0

        while i< len(left_list) and j< len(right_list):
            if left_list[i]< right_list[j]:
                arr[k] = left_list[i]
                i += 1
            else:
                arr[k] = right_list[j]
                j += 1
            k += 1

        while i<len(left_list):
            arr[k] = left_list[i]
            i += 1
            k += 1

        while j<len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1



# Code to print the list 
def printList(arr): 
    for item in arr:
        print(item, end = " ")
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

"""
n = number of elements in the array
Space Complexity: O(n) 

Time Complexity:
O(n log n)
"""