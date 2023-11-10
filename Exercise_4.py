# Python program for implementation of MergeSort 

# Time Complexity: O(Nlog(N))
# We keep dividing the array into 2 halves recursively, 
# thereby we do n iterations over 'height of tree': log(n) = n * log(n)

# Space Complexity: O(N)
def mergeSort(arr):
    if len(arr) < 2:
      return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    # Iterate over two lists 'left' and 'right
    i = 0
    j = 0

    # Iterate over resultant sorted list we want to form
    k = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        arr[k] = left[i]

        # Move the pointer for the winning list
        i += 1
      else:
        arr[k] = right[j]

        # Move the pointer for the winning list
        j += 1

      k += 1
    
    # Add remaining elements from one of the lists to final output
    while i < len(left):
      arr[k] = left[i]
      k += 1
      i += 1
    
    while j < len(right):
      arr[k] = right[j]
      k += 1
      j += 1
  

# Code to print the list 
def printList(arr):
    print([x for x in arr])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
