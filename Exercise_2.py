#Time Complexity: O(nlogn)
#Space; Happens in place so O(1)
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # find a partition such that left of partition is has smaller elements. Right of partition has larger elements
    #choosing last element as pivot
  
    #write your code here
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        part = partition(arr,low,high)
        #Recursively finding partitons on right part and left part
        quickSort(arr,low,part-1)
        quickSort(arr,part+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
