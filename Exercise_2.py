# Python program for implementation of Quicksort Sort
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]  #Choose the pivot as the last element
    i = low - 1  #Index of smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  #Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  #Place pivot in the correct position
    return i + 1  #Return the index of the pivot

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        pi = partition(arr, low, high)  #Partition the array and get pivot index

        #Recursively sort elements before and after the pivot
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:",arr)
  
 
