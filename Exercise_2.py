# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    p = arr[low]
    
    count = 0
    
    for i in range(low, high+1):
        if (arr[i] < p):
            count += 1
            
    pi = low+count
            
    arr[pi], arr[low] = arr[low], arr[pi]
    
    i = low
    j = high
    
    while (i < j):
        if (arr[i] < arr[pi]):
            i += 1
        elif (arr[j] >= arr[pi]):
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
            
    return pi
        
        
#Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if (low >= high):
        return
    
    pi = partition(arr,low,high)
    
    quickSort(arr,low,pi-1)
    quickSort(arr,pi+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),