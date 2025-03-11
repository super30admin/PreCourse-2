# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):  
    #write your code here
    pivot = arr[high]
    first_max_pos = low
    for i in range(low, high+1):
        if arr[i] <= pivot:
            temp = arr[first_max_pos]
            arr[first_max_pos] = arr[i]
            arr[i] = temp
            first_max_pos += 1
    return first_max_pos-1
    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        partition_pos = partition(arr, low, high)
        quickSort(arr, low, partition_pos - 1)
        quickSort(arr, partition_pos + 1, high)         

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
