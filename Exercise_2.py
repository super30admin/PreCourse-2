# Python program for implementation of Quicksort Sort 
# Time Complexity : O(NlogN) Best when select mean 
# as pivot
# Space Coplexity : O(N)      
# give you explanation for the approach
# Any problems faced during this: No

def partition(arr,low,high):
    # Randomly assigning high as the pivot
    pivot = arr[high]
    # Index storing the lower element
    i = low - 1

    for j in range(low, high):
        # If find an element lower than pivot
        # Swap
        if arr[j] <= pivot:
            i = i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
            
    # At the end swap the pivot with the element next to lower index
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i+1
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if high > low:
        # Calling the partition
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
        
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
