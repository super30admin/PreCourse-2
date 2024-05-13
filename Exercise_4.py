# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
 
  if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left = arr[:mid]  # Divide the array into two halves
        right = arr[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Merge the sorted halves
        i = j = k = 0  # Initialize indices for merging
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Check if any elements are left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

 
  
# Code to print the list 
def printList(arr): 
   for i in arr:
      print(i)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
