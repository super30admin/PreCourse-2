# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i=low
    j=high-1
    while i<j:
        while i<high and arr[i]<arr[high]:
            i+=1
        while j>low and arr[j]>=arr[high]:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>arr[high]:
        arr[i],arr[high]=arr[high],arr[i]
    return i
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        partition_pos=partition(arr,low,high)
        quickSort(arr,low,partition_pos-1)
        quickSort(arr,partition_pos+1,high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
