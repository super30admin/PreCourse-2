# Python program for implementation of Quicksort Sort 
# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : No
# give you explanation for the approach
def partition(arr,low,high): 


    #write your code here
    #select i as 
    i= low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        #finding pivot element 
        pi = partition(arr, low, high)

        #recursive call on the left of pivot 
        quickSort(arr, low, pi - 1)

        #recursive call on the right of pivot
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end=" ") 
  
 
