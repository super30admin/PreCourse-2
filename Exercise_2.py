# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def partition(arr,low,high):
    i=low+1
    j=high
    pivot=arr[low]
    while i<j:
        while arr[i]<pivot and i<high:
            i+=1
        while arr[j]>pivot:
            j-=1
        if (i<j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j

    #write your code here

# Function to do Quick sort 
def quickSort(arr,low,high):
    if(low<high):
        j=partition(arr,low,high)
        quickSort(arr,low,j-1)
        quickSort(arr,j+1,high)

    
    #write your code here
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
