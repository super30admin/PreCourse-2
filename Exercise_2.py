# Python program for implementation of Quicksort Sort 

# Time Complexity: i)Best & Average Case : O(n log n)
#                  ii)Worst Case : O(n^2)
# Space Complexity: i)Best & Average Case : O(n lon n)
#                  ii)Space Complexity: O(n)
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[low]
    i = low
    j = high
    while (i < j):
        while i < high and arr[i] <= pivot:
            i = i + 1
        while j > low and arr[j] > pivot:
            j = j - 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]  
    arr[low], arr[j] = arr[j], arr[low]
    return j
        
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if (low < high):
        j = partition(arr, low, high)
        quickSort(arr, low, j-1)
        quickSort(arr, j+1, high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
