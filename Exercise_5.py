# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
  i = (low - 1) #i will initially be made to point just before the low element
  pivot = arr[high] #Set the last element to be the pivot

  for j in range(low, high): #'Iterate' through the entire subarray
    if arr[j] <= pivot: #If element at jth index is less than or equal to the pivot, increment i, and swap elements at i and jth indices
      i += 1
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
  
  temp = arr[i+1] #Swap the last element (pivot) with the element at the partitioning position. The pivot is not in its sorted place
  arr[i+1] = arr[high]
  arr[high] = temp

  return (i+1) #Return the partitioning index



def quickSortIterative(arr, low, high):
  #write your code here
  if low<high: #If it is a valid array
    j = partition(arr, low, high) #Partition the array by using a pivot. All the elements towards its left should be less than the pivot and all the elements towards its right should be greater than the pivot. The array will be partitioned into two separate portions to conquer.
    quickSortIterative(arr, low, j-1) #Run quick sort on the left side of the array
    quickSortIterative(arr, j+1, high) #Run quick sort on the right side of the array

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
