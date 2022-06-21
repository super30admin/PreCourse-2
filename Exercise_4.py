# Time Complexity - O(nlog(n))
# Space Complexity - O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
    #write your code here
    if len(arr) > 1:

        #  r is the partition point where the array is divided into two subarrays
        r = len(arr)//2
        left_array = arr[:r]
        right_array = arr[r:]

        # Sort the two halves
        mergeSort(left_array)
        mergeSort(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

    
# Code to print the list 
def printList(arr): 
    
    #write your code here
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
