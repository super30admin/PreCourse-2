# Time complexity : O(n log(n)). At every step, we split the array into two halves which takes log(n) time 
# and the merging operation takes linear time
# Space complexity : O(n). Additional space is used to create temporary arrays during merging

#Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if len(arr) > 1:
        
    # Sort the left half of the array and right half separately
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    # Recursively call the function on left and right halves
    mergeSort(L)
    mergeSort(R)

    # Merging the sub arrays into original array arr
    # Copy elements from left and right sub arrays to the original array
    # Maintain 3 indices for the three arrays

    i = 0; j = 0; k = 0
    # print(f'Start:{arr, L, R}')
    while i < len(L) and j < len(R):
        # Compare elements from left and right halves and place them in sorted order
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    # Copy all elements left out in the left sub array
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    
    # Copy all elements left out in the right sub array

    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
        print('%d' % arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
