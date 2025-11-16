# Python program for implementation of Quicksort Sort 
  
# Keep on checking if all the elemts smaller than pivot are on the left of i + 1
# If all elements till i are lesser than pivot, place the pivot at i+1th position and return the index of the pivot.
# Hence we partition by placing the pivot at its place when array is sorted, so all elements to the left of pivot are smaller and all elements to the right of pivot are greater.
def partition(arr,low,high):  
    #write your code here
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,0,pi-1)
        quickSort(arr,pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i])