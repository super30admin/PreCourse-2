# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
        # the middle of the array
        mid = len(arr) // 2

        # dividing the array into left and right halves
        left = arr[:mid]
        right = arr[mid:]

        # recursively sorting the two halves
        mergeSort(left)
        mergeSort(right)

        # merging the sorted halves
        i = j = k = 0

        # copying data to temporary arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # checking for any remaining elements in left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # checking for any remaining elements in right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
        print(i, end=" ")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
