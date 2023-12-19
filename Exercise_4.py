# Python program for implementation of MergeSort 
## Time complexity : O(n logn) 
## Space complexity : O(n)

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        left = arr[:mid]
        right = arr[mid:]
 
        # Sorting the first and second halves
        mergeSort(left)
        mergeSort(right)
 
        i = j = k = 0
 
        # Putting data to smaller left and right arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def printList(arr): 
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
