# Python program for implementation of MergeSort 
def mergeSort(arr):
    # write your code here

    if len(arr) > 1:
        mid = len(arr) // 2

        # Divide
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        mergeSort(left)
        mergeSort(right)

        # Merge the two sorted halves
        i = j = k = 0

        # Compare elements from left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
  

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
        for x in arr:
            print(x, end=" ")
        print()


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

# TC - O(nlogn)
# SC - O(n)