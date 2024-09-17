# Python program for implementation of Quicksort Sort

# Time complexity - O(N logN) ,  for every pivot, we are dividing the array into half - O(logN)
# space complexity - Its in -place sorting hence constant space additional space is required
  
# give you explanation for the approach
def partition(arr,low,high):

    _partition = arr[high]
    pIndex = low
    for i in range(low, high):
        if arr[i] <= _partition:
            # swap the elements that are smaller than the defined partition
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
    # swap the paritioned element with the current arr[high] because the element is greater than paritioned element for sure due to the condition
    # arr[i] <= _partition in the above for loop
    arr[pIndex], arr[high] = arr[high], arr[pIndex]
    # return the index
    return pIndex

# Function to do Quick sort 
def quickSort(arr,low,high):
    # base case,
    if low < high:
        # find the partition index and recursively divide into 2 sub arrays
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
'''
OUTPUT:
Sorted array is:
1 5 7 8 9 10
'''