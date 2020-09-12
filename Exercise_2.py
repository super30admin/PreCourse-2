# Python program for implementation of Quicksort Sort 
# Time Complexity: Avg Case: O(nlog(n)) | Worse Case: O(n^2)(When the array is in descending order)
# Space Complexity: O(log(n)) for the call stack

# give you explanation for the approach
# - So during partition we choose a pivot and segregate the array in such a way that values smaller than
#   the pivot are added to the left side and values grater, to the right. 
# - To acheive this we have a variable i, which is used to keep track of the last element that is smaller than the pivot. 
#   So if we find a smaller value during our iteration, we swap with the ith element.

def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here

    if low >= high:
        return

    mid = partition(arr, low, high)
     
    quickSort(arr, low, mid - 1)
    quickSort(arr, mid + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
