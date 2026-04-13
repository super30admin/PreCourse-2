#//Time Complexity :O(nlogn)
#// Space Complexity : O(logn) 
#// Did this code successfully run on Leetcode : Yes
#// Any problem you faced while coding this : Forgot the algorithm and while implementing had difficulty in converting logic to code.
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    #picking middle element for pivot
    pivot = arr[(low + high) // 2]
    i = low -1
    j = high + 1
    while True:
        # moving i pointer to right
        i += 1
        while arr[i] < pivot:
            i += 1
        # moving j pointer to left    
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        #pointer cross return j as pivot
        if  i >= j :
            return j
        
        arr[i], arr[j] = arr[j], arr[i]  
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        p = partition(arr,low,high)
        
        quickSort(arr,low,p)
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

 
