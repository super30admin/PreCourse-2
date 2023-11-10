# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time complexity = best case - O(nlogn) , worst case - O(n^2) - Worst case occurs when the input array is already sorted
# Approach : we choose a pivot element at every stage (last element in this case) and then rearrange the array such that
# all the elements lesser than pivot are on the left side of pivot and all the elements greater than pivot are on the right side.
def partition(arr,low,high):
    #write your code here
    idx = low - 1
    pivot = arr[high]

    for i in range(low, high):
        if arr[i] <= pivot:
            idx +=1
            arr[idx], arr[i] = arr[i] , arr[idx]

    arr[idx+1], arr[high] = arr[high], arr[idx+1]
    return idx+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if len(arr) == 1:
        return arr

    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr,pivot+1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
