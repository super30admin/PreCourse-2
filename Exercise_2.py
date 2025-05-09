# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#Swap Function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high] #Select Pivot
    i= low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1) #Recurssion
        quickSort(arr, partition_index+1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
