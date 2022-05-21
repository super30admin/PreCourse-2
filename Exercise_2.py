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
    
    #pointer i as the low index
    i=low
    
    #pointer j as the last index -1 
    j=high-1
    
    for i in range(low,j):
        #Swapping the elements less than the pivot element to the left and those greater than the pivot elements to the right
        
        while i<high and arr[i]<pivot:
            i=i+1
        while j>low and arr[j]>=pivot:
            j=j-1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i] > pivot:
        arr[i], arr[high]=arr[high], arr[i]
    return i
    
  

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
  
