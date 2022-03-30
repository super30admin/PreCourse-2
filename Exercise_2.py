# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        #curent number being examined is less than pivot?
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    #swap the pivot
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #index of pivot after swap
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        #to store index of partition
        partitionIndex = partition(arr,low,high)
        #call quick sort on left side array 
        quickSort(arr,low,partitionIndex-1)
        #call quick sort on right side array
        quickSort(arr,partitionIndex+1,high)
    else:
        return arr
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
 
