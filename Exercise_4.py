#time compexity : O(nlogn)
def merge(arr,low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
 
    # create temp arrays
    left = [0] * (n1)
    right = [0] * (n2)
 
    # Copy data to temp arrays left[] and right[]
    for i in range(n1):
        left[i] = arr[low + i]
 
    for j in range(n2):
        right[j] = arr[mid + 1 + j]
 
    # Initial index of first subarray
    i = 0     
    j = 0     
    k = low     

    # Merge the temp arrays back into arr[]
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of left[]
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of right[]
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
   
# Python program for implementation of MergeSort 
def mergeSort(arr, low, high):
  
  if low<high:
     mid = (low+high) // 2
     mergeSort(arr, low, mid)
     mergeSort(arr, mid+1, high)
     merge(arr,low,mid,high)
  #write your code here
  
# Code to print the list 
def printList(arr):    
  for i in arr:
    print ("%d" %i)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

    #for i in range(0, 5):
    #   print(i)
