# Time Complexity : O(NlogN), divides and conquers before going through every value.  
# Space Complexity : O(N), N being the length of the array.
# Did this code successfully run on Leetcode : Did not find a corresponding problem on leetcode. 
# Any problem you faced while coding this : Had to review how to do quicksort. 


# Your code here along with comments explaining your approach

# Python program for implementation of Quicksort Sort 

# give your explanation for the approach
def partition(arr,low,high):
    #write your code here
    mid = int((low+high)/2)
    pivot = arr[mid]

    while(low<high):
        #find first from left value greater than pivot.
        while(arr[low]<pivot):
            low = low+1
        #find first from right value less than pivot
        while(arr[high]>pivot):
            high = high-1
        #swap
        temp = arr[low]
        arr[low]=arr[high]
        arr[high]=temp
    return int((low+high)/2)
        
# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if (high-low)>=1:
        mid = partition(arr, low, high)
        quickSort(arr, low, mid)
        quickSort(arr, mid+1, high)    
    

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
    

