#Space Complexity: O(1)
#Time Complexity: average case - O(n log n), worst case - O(n^2) ... where n is the number of elements
#The code did run successfully

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]                           #taking the last element as the pivot
    i = low - 1                                 #this is to mark the posiiton from where the partition starts
    j = low
    while j < high:
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]       #done to adjust the oeft half partition elements
        j += 1
    
    arr[i+1],arr[high] = arr[high],arr[i+1]     #to place the pivot at the correct position(which is after the partition point)
    return i + 1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pi_point = partition(arr,low,high)      #to search for the partition from where the elements greater than the pivot are stored
        quickSort(arr,low,pi_point - 1)         #to recursively sort the left half (elements lesser than the partition point)
        quickSort(arr,pi_point + 1,high)        #to recursively sort the right half (elements greater than the partition point)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
