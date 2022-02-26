# Python program for implementation of Quicksort Sort 

#time complexity : O(nlogn)
#space complexity O(1)
def partition(arr,low,high):
  
  
    start = low
    end = high
    pivot = arr[low]
    pivot_index = low

    while(start<end):
        while start<len(arr) and arr[start] <= pivot:
            start = start + 1
        while arr[end] > pivot:
            end = end - 1
        if start < end:
            tmp1 = arr[start]
            arr[start]  = arr[end]
            arr[end] =  tmp1
            
    tmp2 = arr[end]
    arr[end] = arr[pivot_index]
    arr[pivot_index] = tmp2

    return end


# Function to do Quick sort 
def quickSort(arr,low,high): 
    start = low
    end = high
    #write your code here
    if (start<end):
        partition_index = partition(arr,start,end)
        quickSort(arr,partition_index+1,end)
        quickSort(arr,start,partition_index-1)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
