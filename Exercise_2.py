# Python program for implementation of Quicksort Sort 
# Time Complexity O(nlogn) Expected
# Time Complexity O(n)
  
# give you explanation for the approach
def partition(arr,low,high):
    p=arr[high]
    index = int(low-1)
    for x in range(low,high):
        if arr[x] < p:
            index+=1
            temp = arr[index]
            arr[index] = arr[x]
            arr[x] = temp
    
    incr_i = index+1
    temp = arr[incr_i]
    arr[incr_i] = arr[high]
    arr[high] = temp
    return incr_i
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partition_data = partition(arr,low,high)
        
        quickSort(arr,low,partition_data-1)
        quickSort(arr,partition_data+1,high)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5,50,-1] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
