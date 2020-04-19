# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach
#In this program we set up the last elemnet in the array as pivot.
#We place the pivot in its current position and check if the element is smaller or larger then it.
# If it is smaller it is placed towards left og the pivot else right.
def partition(arr,low,high):
    i=(low-1)# index of the smaller element
    pivot=arr[high] #setting pivot
    
    for j in range(low,high):
        if arr[j]<=pivot:#checking if the current element is small or equal to the pivot
            i=i+1 #increment the index of the smaller index
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
  
  
   
  

# Function to do Quick sort
def quickSort(arr,low,high):
    if low<high:
        partition_index=partition(arr,low,high)
        
        quickSort(arr,low,partition_index-1)
        quickSort(arr,partition_index+1,high)
    
  
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
  
