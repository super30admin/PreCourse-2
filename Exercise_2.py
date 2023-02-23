# Python program for implementation of Quicksort Sort 
  
# Time Complexity: O(nlog n)
# Space Complexity: O(log n)

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here

    pivot = arr[high] #pivot is selected as the last element in the list
    i = low - 1 #set to the smaller number

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i + 1

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
