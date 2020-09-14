# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i=low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<=high:
        p = partition(arr,low,high)
        print(p)

        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [2,2,2,2,2,2,2,2] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
