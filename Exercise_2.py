# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # if low>=high:
    #     return
    pivot = low
    left = low + 1
    right = high

    while left <= right:

        if arr[left] >= arr[pivot] and arr[right] < arr[pivot]:
            arr[left] , arr[right] = arr[right], arr[left]
        if arr[left] < arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1
        

    arr[pivot], arr[right] = arr[right], arr[pivot]

    return right
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low, p - 1)
        quickSort(arr, p + 1, high)
        return 
    #write your code here
  
# Driver code to test above 
#arr = [10, 7, 8, 9, 1, 5] 
arr = [16,3, 7, 15,8, 3, 1, 9, 3, 2]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
