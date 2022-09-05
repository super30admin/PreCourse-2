# Time Complexity: Worst - O(n*n), average time - O(nogn)
# Space Complexity - O(n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
    #write your code here
    pivot = arr[high]
    tmp = low

    for i in range(low, high):
        if arr[i] <= pivot:
            arr[i], arr[tmp] = arr[tmp], arr[i]
            tmp += 1
    arr[tmp], arr[high] = arr[high], arr[tmp]

    return tmp
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
    return arr

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
