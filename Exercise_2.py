# Python program for implementation of Quicksort Sort 
  
# Time Complexity : O(N^2)
# Space Complexity : O(N)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    
    #Selecting last element as the pivot element
    pivot=arr[high]
    
    #Let pointer be low-1
    i=low-1
    for j in range(low,high):
        #Shifting the elements less than the pivot element to the left
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    

    if low<high:
        q=partition(arr,low,high)
        quickSort(arr,low,q-1)
        quickSort(arr,q+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
