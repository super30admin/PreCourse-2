# Time Complexity : O(nlogn)
# Space Complexity : 
# Is it on Leetcode: Dont know
# Problem faced while solving: Was difficult for me to write partition function 

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = (low-1)                                         # Index position of smaller element
    pivot = arr[high]                                   # Declared pivot 
    
    for j in range(low, high):                          
                                                        
        if(arr[j] <= pivot):                            # When j value is less than or equal to pivot value
            i = i+1                                     # Increment smaller element index and swap
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Function to do Quick sort 
def quickSort(arr,low,high):                            
    if(len(arr) == 1):                                  # If array consists of one element 
        return arr                                      # Will return that element
    if(low < high):

        pi = partition(arr, low, high)                  # Partitioning index used for sorting

        quickSort(arr, low, pi-1)                       # Used for sorting elements before and after partitioning 
        quickSort(arr, pi+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
