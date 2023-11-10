# Python program for implementation of Quicksort Sort 
#  Time Complexity : O(N**2)
#  Space Complexity : O(1)

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[low]
    i,j = low,high

    while i < j:
        while i < len(arr) and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]

    return j
  
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        quickSort(arr,low, pi-1)
        quickSort(arr,pi+1,high) 
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
