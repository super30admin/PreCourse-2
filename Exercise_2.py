# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#-----------------------------------------------------
# Time Complexity : O(n*n)  ---> n is the number of elements in the array
# Space Complexity : O (logn) ---> n is the number of elements in the array
#---------------------------------------------------
def partition(arr,low,high):

    left=low-1
    pivot = arr[high]  # Initial pivot is the last element.
    
    for j in range(low, high):
        # check if element if less than pivot
        if arr[j] <= pivot:
            #increment left 
            left+=1
            #swap elements
            arr[left], arr[j] = arr[j], arr[left]
    #swap the pivot
    arr[left+1], arr[high] = arr[high], arr[left+1]       
    return left+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low <high:
        #find position of pivot element
        part =partition(arr,low,high)
        #left subarray
        quickSort(arr,low,part-1)
        # right subarray
        quickSort(arr,part+1,high)
    # return arr
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
#     []
#     [5, 1, 7, 9, 8, 10]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
