# Python program for implementation of Quicksort Sort 
#Time Complexity: O(n*log n)
# Space Complexity: O(n) 
# Set pivot as highest index
#Sets pivot to its correct position
#All values smaller than pivot at left hand side
#All values greater than pivot at the right side
def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


  

# Function to do Quick sort
# If array is single element than return the value or sort it further  
def quickSort(arr,low,high):
    if len(arr) == 1:
        return arr
#find the partition for pivot element
#Continue the process for left and right subarrays of pivot
    while low<high:
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
  
 
