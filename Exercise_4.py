#Time Complexity:O(nlogn)
#Space Complexity:O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  #write your code here
  if len(arr) > 1: # divide the list if the length is greater than 1

    mid = len(arr)//2 # get the mid value

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left) #run the function for left and right half separately
    mergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right): #while the index is less than length of both array loop it
      if left[i] <= right[j]: # get the greater value from both the array and add it to original array
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1

    while i < len(left): #get the remaining values from both the arrays if there are any
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1

# Code to print the list 
def printList(arr): 
    
    #write your code here
  for i in range(len(arr)): # loop though the array and print each element
    print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
