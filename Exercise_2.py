# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = high
    i = low
    j = low
    while(i<high):
        if(arr[i]<arr[pivot]):
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
        i+=1
    arr[pivot],arr[j] = arr[j],arr[pivot]
    return j
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if(low>high):
        return
    pivot = partition(arr,low, high)
    quickSort(arr,low,pivot-1)
    quickSort(arr,pivot+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
