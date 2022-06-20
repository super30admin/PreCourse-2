# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
## Time Complexity = O(N^2) in worst case and O(NlogN) in average case
## Space Complexity  =  O(logN) average case  and O(N) worst case as we use additional space in recursion stack
def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        piv = partition(arr,low,high)
        quickSort(arr,low, piv-1)
        quickSort(arr,piv+1, high)


    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
