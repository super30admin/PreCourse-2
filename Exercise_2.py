# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#Quick sort is a divide and conquer algorithm. Ideal idea is to choose a pivot element here its chosen as highest one and then partition the array in 2 subarrays based on their values around chosen pivot element.
#After that the sub arrays are sorted recursively.
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1
  
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        temp = partition(arr, low, high)

        quickSort(arr, low, temp - 1)
        quickSort(arr, temp + 1, high)

    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
