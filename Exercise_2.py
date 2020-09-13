# Python program for implementation of Quicksort Sort 
#Author - Srinidhi Bhat
# give you explanation for the approach
"""
time complexity - Average and best case - O(NlogN)
                  Worst Case - O(n^2)

Space Complexity - O(1) - since it is an in place sorting algorithm
                          with no extra space.
"""
def partition(arr,low,high):
    start = low -1 
    pivot = arr[high]

    for j in range(low,high):
        if arr[j]<=pivot:
            start+=1
            arr[start],arr[j] = arr[j],arr[start]
    arr[start+1],arr[high] = arr[high],arr[start+1]
    return start+1

# Function to do Quick sort
def quickSort(arr,low,high):

    if low<high:
        partition_position = partition(arr,low,high)
        quickSort(arr,low,partition_position-1)
        quickSort(arr,partition_position+1,high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),