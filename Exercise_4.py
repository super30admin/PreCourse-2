# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1:
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    
    mergeSort(left_arr)       # Sorting the left subarray.
    mergeSort(right_arr)      # Sorting the right subarray.

    i = 0     # Pointer for left subarray.
    j = 0     # Pointer for right subarray.
    k = 0     # Pointer for the main sorted array.

    while i<len(left_arr) and j<len(right_arr):
      if left_arr[i] <= right_arr[j]:
        arr[k] = left_arr[i]        # Add the element of left subarray into the main array.
        i+=1                        # Move the pointer of left subarray to next index.
      else:
        arr[k] = right_arr[j]       # Add the element of right subarray into the main array.
        j+=1                        # Move the pointer of right subarray to next index.
      k+=1                          # Move the pointer of main array to next index.

    while i < len(left_arr):        # Add elements into main array if any remaining in left subarray. 
      arr[k] = left_arr[i]
      k+=1
      i+=1
    
    while j < len(right_arr):       # Add elements into main array if any remaining in right subarray. 
      arr[k] = right_arr[j]
      k+=1
      j+=1
    

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(f'{i} ', end = "")
    print()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
