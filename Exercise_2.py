# Python program for implementation of Quicksort Sort 
 #Time Complexity = Here it is O(N^2) Since the array is sorted
 #and the pivot element is taken is 5 which is lesser than all values except 1 so in right hand 
 #side of  pivot we have to interate through every element
#Space Complexity = O(Log(N) 
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    i =low
    while i < len(arr):
        if arr[i] < pivot:
            (arr[i],arr[low]) = (arr[low],arr[i])
            low = low +1
        i+=1
    (arr[low],arr[high]) = (arr[high],arr[low])
    return low
# Function to do Quick sort 
def quickSort(arr,low,high):
  if low < high:
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
  
 
