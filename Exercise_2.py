# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    #here pivot variable will be the base to make partition of the array
  pivot = arr[low]
  i = low+1
  j = high
  while(i<j):
    #while loop will work till the value greater then the pivot element will be encounter
    while (arr[i]<=pivot and i < high):
      i = i + 1
    #while loop will work till the value lower then the pivot element will encounter
    while(arr[j]>pivot and j>low):
      j = j-1
    #value greater then pivot from left to right and value less then pivot right to left will swap
    if(i<j):
      arr[i], arr[j] = arr[j], arr[i]
  #partition will occur according to the pivot element
  arr[low], arr[j] = arr[j], arr[low]
  #position of the partition will be returned
  return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
  if(low<high):
    #array will be divide into two parts for sorting with the help of recursion function
    j = partition(arr, low, high)
    partition(arr, low, j)
    partition(arr,j, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
