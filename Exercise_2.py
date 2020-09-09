# Python program for implementation of Quicksort Sort 
"""
def quicksort(array):
  if len(array)<=1:
    return array
  else:
    pivot = array.pop()
    item_greater = []
    item_smaller = []
    for item in array:
      if item>pivot:
        item_greater.append(item)
      else:
        item_smaller.append(item)
    
  return quicksort(item_smaller) + pivot + quicksort(item_greater) """

#I find the above solution easier but has space 2n

 
# give you explanation for the approach
# Here I am taking last element of the array as Pivot and Pivot is just the number to be compared by all other numbers and will fianlly get the sorted position of pivot in the array. After this we will repeat the process to the leaft and right part of array with respect to pivot.

def partition(arr,low,high):
  i = low-1
  pivot = arr[high]
  for j in range(low,high):
    if arr[j]<=pivot:
      i =i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1
      
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
    if low < high:
        qs = partition(arr, low, high)
        quickSort(arr, low, qs-1)
        quickSort(arr, qs+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
