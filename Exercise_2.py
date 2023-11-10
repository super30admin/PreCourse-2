# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    
    while True:
        while i<=j and arr[i]<=pivot:
            i=i+1
            
        while i<=j and arr[j]>=pivot:
            j=j-1
            
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            print(arr)
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    print(arr)
    return j
        

  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low>=high:
        return
    
    #write your code here
    p=partition(arr,low,high)
    quickSort(arr,low,p-1)
    quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
