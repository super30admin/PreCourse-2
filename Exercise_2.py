# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    divider = low
    pivot = high

    for i in range(low, high):
        if arr[i]<arr[pivot]:
            arr[i], arr[divider] = arr[divider], arr[i]
            divider+=1
        
    arr[pivot], arr[divider] = arr[divider], arr[pivot]
    
    return divider
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<=high:
        x = partition(arr, low, high)
        quickSort(arr,low, x-1)
        quickSort(arr,x+1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
