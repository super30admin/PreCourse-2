# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : O(nlogn)
# Space Complexity : O(1)

def partition(arr,low,high):
    i=low
    j=high
    t=0
    v=0
    pivotElement=arr[low]

    while(i<j):
        while(arr[i]<= pivotElement and i<=high -1):
            i=i+1
        while(arr[j] > pivotElement and j>=low + 1):
            j=j-1
        
        if (i < j):
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
    
    v=arr[low]
    arr[low]=arr[j]
    arr[j]=v
    
    return j


  # Function to do Quick sort 
def quickSort(arr,low,high): 
    if(low<high):
        pivotIndex=partition(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)
   
  
# Driver code to test above 

arr = [10,7,8,9,1,5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=" "), 
  
 
