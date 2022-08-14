# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(nlogn) n is the number of nodes in the link list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :  Yes
# Any problem you faced while coding this :  No
def partition(arr,low,high): # returns the pivot element
  i = low-1
  pivot = arr[high]
  for j in range (low,high):
    if arr[j] <= pivot:
        i+=1
        arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high] = arr[high], arr[i+1]
  return i+1  

    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if (low < high):
        pos = partition(arr,low,high)
        quickSort(arr,low,pos-1)
        quickSort(arr,pos+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
