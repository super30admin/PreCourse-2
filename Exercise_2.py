# Time Complexity : O(NlogN) as we divide the list 
# Space Complexity : O(1) as no extra space is required expcept pivot element
# Did this code successfully run on Leetcode : I did not find this exact problem on leetcode
# Any problem you faced while coding this : Took me a little while to understand that in the partiton function, the if statement is the for loop fails 
# if the list is sorted in descending order

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr, low, high):
    #write your code here
    # l acts as the low index and i in the for loop acts as the high index
    # if the high, i.e, ith element is less than the pivot
    # then we swap element at low with element at high

    l = low - 1
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] <= pivot:
            l += 1 # increase by 1 to reach correct index
            arr[l], arr[i] = arr[i], arr[l]
    arr[l+1], arr[high] = arr[high], arr[l+1]
    return (l+1)
    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        partition_index = partition(arr, low, high)  # to get the pivot element's index
        quickSort(arr, low, partition_index - 1)  # to sort the sublist to the left of the pivot
        quickSort(arr, partition_index + 1, high)  # to partition the sublist to the right of the pivot

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
