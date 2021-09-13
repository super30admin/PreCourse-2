'''
// Time Complexity : Worst Case O(n^2), average O(nlogn)
// Space Complexity : O(1)
'''
# Python program for implementation of Quicksort Sort 
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot_index = low
    pivot = arr[pivot_index]
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low+=1

        while arr[high] > pivot:
            high-=1

        if low < high:
            swap(low, high, arr)

    swap(pivot_index, high, arr)

    return high

def swap(i, j, arr):
    if i!=j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

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
  
 
