# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  pivot = arr[low]
  i = low, j= high
  
  ##swapping conditions during comparison
  while i<j:
    if arr[i]>pivot and arr[j]<pivot:
      arr[i],arr[j] = arr[j],arr[i]
    
    elif arr[i]<pivot:
      i++
      
    elif arr[j]>pivot:
      j--
  
  arr[low],arr[j] = arr[j],arr[low] ##swap pivot with j after i is no longer smaller than j
  return j ##j is the true position of the pivot. Ensures that values to the left of pivot are smaller and those on the right are larger
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
      j = partition(arr,low,high) ##returns correct element of pivot
      quickSort(arr,low,j) ##elements left of pivot get rearranged
      quickSort(arr,j+1,high) ##elements right of pivot get rearranged
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
