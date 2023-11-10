# Time Complexity:
# Space Complexity:
# Is this problem on leetcode: Yes
# Did you face any problem solving this? -->

# Write a code and explain below: Merge sort is Divide and Conquer algorithm, it divides into two halfs
# arranges them and then merge them back.


# Python program for implementation of MergeSort 
def mergeSort(arr):                                       # Function for merge sort
  if len(arr) > 1:                                        # array lenght greater than 1

    mid = len(arr)//2                                     # Calculating mid point
    L = arr[:mid]                                         # Sorting the first half
    R = arr[mid:]                                         # Sorting the second half
    mergeSort(L)                                          # Using mergesort on left half
    mergeSort(R)                                          # Using mergesort on right half
    i = j = k = 0

    while i < len(L) and j < len(R):                      # Copying the data
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    while i < len(L):                                      # Checking if any element is at left
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1

      
def printList(arr):                                         # Function to print the list
    for i in range(len(arr)):
      print(arr[i], end= " ")
    print()

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
