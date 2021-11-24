#Time complexity: O(n * n)
#space complexity: O(n)

#The lowest value is taken is taken as pivot and is  then sorted based on the pivot. Recursion technique is used here to solve for this one.
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    if low < high:
        rec = partition(low, high, arr)

        quickSort(arr, rec - 1, arr)
        quickSort(rec + 1, high, arr)
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    pivotI = low
    pivot = arr[pivotI]

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if (low < high):
            arr[low], arr[high] = arr[high], arr[low]

        arr[high], arr[pivotI] = arr[pivotI], arr[high]
        return high
        


    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
