# Time Complexity - O(n log n) - Splitting O(logn) ; Merging O(n)
# Space Complexity - O(n) for arrays used


# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here

  if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle
        leftHalf = arr[:mid]        # Split to Left half
        rightHalf = arr[mid:]       # Split to right half


        # Sort both halves
        mergeSort(leftHalf)    
        mergeSort(rightHalf)


        # Merge both halves
        i = j = k = 0

        # Compare elements and merge array
        while i < len(leftHalf) and j < len(rightHalf):
          if leftHalf[i] < rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
          else:
            arr[k] = rightHalf[j]
            j += 1
          k += 1

        # Copy remaining elements of leftHalf or rightHalf
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1


# Code to print the list 
def printList(arr): 
    
    #write your code here

  for i in arr:
      print(i, end =" ")
  print()

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
