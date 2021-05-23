# Python program for implementation of Quicksort Sort 
  
# The parition function chooses the last element of array as the pivot ,places the pivot to its correct position and places the smaller values to the left and greater values to the right of pivot
def partition(arr,low,high):
  
    #write your code here
    pivot = arr[high];
    i = low-1;

    for j in range(low,high):
        #check element smaller than pivot 
        if(arr[j]<=pivot):
            i = i+ 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) < 2:
        return arr

    if low < high:

        #p position acting as the partitioning index,arr[p] sorted
        p = partition(arr,low,high)

        #Separately sorting elements using recursion
        quickSort(arr,low,p -1)
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
