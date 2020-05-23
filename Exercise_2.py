"""
// Time Complexity :  O(nlog n), where n is the number of elements
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : problem not there on Leetcode
// Any problem you faced while coding this : No
"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  #write your code here
  p = high #setting pivot to be the last element 
  i = low #setting i to start from the first element in arr
  
  for i in range(low, high): 
      
      if arr[i] < arr[p]: #if element smaller than the pivot element is found, we swap that element with low and increment low to point to the next position
          arr[i], arr[low] = arr[low], arr[i] #swap
          low = low+1
  arr[low], arr[p] = arr[p], arr[low] #after the loop terminates, low will be pointing to the correct position of the pivot element, hence we swap the values at low and p so that the pivot element is at its correct position
  return low #return the point where partition happens

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high: #stopping condition
        p = partition(arr,low,high) #partition index
        quickSort(arr, low, p-1) #call function again on the left half of arr
        quickSort(arr, p+1, high) #call function again on the right half of arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 

for i in range(n): 
    print ("%d" %arr[i]), 

 
