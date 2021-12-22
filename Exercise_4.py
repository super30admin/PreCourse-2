# Python program for implementation of MergeSort 

# Time Complexity : O(n log n) (as divides into 2 halves and merges)
# Space Complexity : O(n) (as we create temp arrays based on n elements of original array)
# Did this code successfully run on VScode : Yes
# Any problem you faced while coding this : No

def mergeSort(arr):

  # In MergeSort we divide array in 2 halves, sort the 2 halves and merge them both
  # This way we get 2 sorted arrays merged into 1 sorted array

  # As long as there are multiple elements in the array
  if (len(arr) > 1):

    # Dividing array into 2 halves. Calline left half L and right half R
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    # Sorting the 2 arrays using recursive call
    mergeSort(L)
    mergeSort(R)

    # Actual logic to sort array
  
    # Declaring variables for the loop
    i = j = k = 0

    # as long as there are elements in both halves
    while i < len(L) and j < len(R):

      # if first element in the left half is smaller than first element in right half
      if L[i] < R[j]:

        # Add smallest element from left half as first element of array and increment index
        arr[k] = L[i]
        i += 1

      # if first element in right half is smaller than first element of left half  
      else:

        # Add smallest element from right half as first element and increment index
        arr[k] = R[j]
        j += 1

      # increment index to sort and store next element    
      k += 1

    # After this, it may be possible that right or left array is smaller and loop breaks. 
    # In that case, need to check remaining elements in either of the half array's and add them to sorted array
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1 
      k += 1
  
# Code to print the list 
def printList(arr): 
  for i in range (len(arr)):
    print(arr[i], end=" ")
  
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("\nSorted array is: ", end="\n") 
    printList(arr) 
