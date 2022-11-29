# Python program for implementation of MergeSort 

def merge(arr, l, mid, h):
  nl = mid - l + 1 #Find the number of elements in the left side of the array
  nr = h - mid #Find the number of elements on the right side of the array

  L = [0] * nl #Initialize an array with 0s for computation on the left side of the array
  R = [0] * nr #Initialize an array with 0s for the computation on the right side of the array

  for i in range(nl): #Loop through the left subarray and copy elements from arr to L
    L[i] = arr[l + i]

  for i in range(nr): #Loop through the right subarray and copy elements from arr to R
    R[i] = arr[mid + 1 + i]
  
  i = 0 #Pointer used for computation on L
  j = 0 #Pointer used for computation on R
  k = l #Pointer used for computation on arr

  while (i < nl) and (j < nr): #Loop as long as i is within the left subarray range and j is within the right subarray range
    if L[i] <= R[j]: #Compare the elements in left and right subarray
      arr[k] = L[i] #Element in the left subarray goes into the original array if it is less than or equal to the element being pointed at by j in the right subarray
      i += 1 #Move to the next element in the left subarray
    else: #Element in the right subarray is greater than the element in the left subarray
      arr[k] = R[j] #It goes into the original array
      j += 1 #Move to the next element in the right subarray
    k += 1 #Increment arr pointer anyway because there would have been an update

  while i < nl: #If there are elements left to be traversed in the left subarray, but all the elements in the right subarray have been traversed, simple copy the elements from the left subarray into arr
    arr[k] = L[i]
    i += 1
    k += 1

  while j < nr: #If there are elements left to be traversed in the right subarray, but all the elements in the left subarray have been traversed, simple copy the elements from the right subarray into arr
    arr[k] = R[j]
    j += 1
    k += 1
 
#Merge sort uses divide and conquer. Elements are divided until they cannot be divided further. A merge operation is then performed on all the portions in which they are sorted and combined and copied into the original array
def mergeSort(arr, l, h):
  #write your code here
  if l < h: #If it is a valid array
    mid = l + (h-l) // 2 #Mid is calculated this way to avoid integer overflow in case of other languages such as Java. It is the best practice, hence has been used here in Python
    mergeSort(arr, l, mid) #Run merge sort on the left subarray to further divide it
    mergeSort(arr, mid+1, h) #Run merge sort on the right subarray to further divide it
    merge(arr, l, mid, h) #Conquer the divided subarrays to sort it

  
# Code to print the list 
def printList(arr): 
    #write your code here
    for i in range(len(arr)):
      print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
