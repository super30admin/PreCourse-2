#Recurrence relation : 2T(n/2) +n
# Time Complexity: O(nlog n) 
#Space complexity: O(n) as the arrays of size n are used.
# This code is executed in python editor.

# Python program for implementation of MergeSort 
def mergeSort(arr): # applying mergesort algorithm here
  if len(arr)>1: # Condition to check if the size of the array is greater than 1
  #write your code here
    mid = int(len(arr)/2)# Calculate the mid value and divide the array into 2 parts.
    left = arr[:mid] #this algorithm is used on the concept of Divide and Conquer
    right = arr[mid:]
    mergeSort(left) # recursive division of the array
    mergeSort(right)

    i,j,k=0,0,0
    while i< len(left) and j< len(right): # Comparing each element until it reaches the end of one loop
      if left[i]< right[j]: # whichever element is smaller is stored in the kth position of the array
        arr[k] = left[i] # The value of k is incremented by 1
        k=k+1
        i=i+1
      else:
        arr[k] = right[j]
        j=j+1
        k=k+1
    while i< len(left):# sorting and adding the values left into the left array
      arr[k] = left[i]
      k=k+1
      i=i+1
    while j< len(right): # sorting and adding the values left into the right array
      arr[k] = right[j]
      k=k+1
      j=j+1

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5,-5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
#Recurrence relation : 2T(n/2) +n
# Time Complexity: O(nlog n) 
#Space complexity: O(n) as the arrays of size n are used.
# This code is executed in python editor.