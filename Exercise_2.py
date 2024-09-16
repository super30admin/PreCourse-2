# Python program for implementation of Quicksort Sort 

# Quick sort uses divide and conquer strategy where each it finds the rightful position for an element such that every element on the left is smaller and to the right all are bigger. Then perform quicksort on left and right side recursively to sort the entire array

# Here, we are picking first element as the pivot- this is flexible. So we perform partition on the rest of elements to find rightful position for the chosen element. 
# We increment i until we find element greater than the chosen and decrement j until we find element smaller than chosen, we swap elements --> we repeat as long as i <=j. At the end we swap chosen element with j which is the rightful position and jth element was anyway supposed to be on left side.
# TC: O(nlogn)
# SC: O(logn) to O(n) (Inplace but recursion absorbs some space)
def partition(arr,low,high):
    i = low+1
    j = high
    pivot = arr[low]
    while(i<=j):
        while(arr[i]<pivot and i<high):
            i = i+1
        while(arr[j]>pivot):
            j = j-1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i+1
            j = j-1
        else:
            i = i+1
    arr[low] = arr[j]
    arr[j] = pivot
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high:
        return
    p = partition(arr, low, high)
    quickSort(arr, low, p-1)
    quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted arr is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
