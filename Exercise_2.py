# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#Time Compleixty: Best and Average: O(nlogn) Worst: O(n^2)
def partition(arr,low,high):
  
    pivot = arr[low]
    start = low + 1
    end = high

    while True:
        while start <= end and arr[start] <= pivot:
            start += 1
        while start <= end and arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end],arr[start]
        else:
            break
    arr[end], arr[low] = arr[low], arr[end]
    return end
 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low >= high:
        return
    p = partition(arr, low, high)
    quickSort(arr,low, p-1)
    quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
