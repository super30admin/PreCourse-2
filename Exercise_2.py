#Time Complexity: O(n^2) due to recursive calls.
# Space Complexity: O(n)
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    
    for j in range(low,high):
        if(arr[j]<=pivot):
            i = i+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high]= temp
    return i+1
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        g = partition(arr,low, high)
        quickSort(arr,low,g-1)
        quickSort(arr,g+1,high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
