# Python program for implementation of Quicksort Sort 
# Time complexity: O(n * log n)
# Space Complexity: O(1)
# give you explanation for the approach
def partition(arr,low,high): # Main logic which sorts the smaller elements to the left side and larger elements to the right side
    pivot = high
    p1 = low
    i = low-1 # Index to return at the end which is going to be at the correct position
    while p1 <= high:
        if arr[p1] < arr[pivot]:
            i += 1
            temp = arr[p1]
            arr[p1] = arr[i]
            arr[i] = temp
        p1 += 1
    temp = arr[high]
    arr[high] = arr[i+1]
    arr[i+1] = temp
    return i+1

    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): # Function that recursively calls the quickSort function in a divide and conquer manner
    if low < high:
        index = partition(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 20, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
