# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = (low-1)
    pvt = arr[high]

    for x in range(low, high):
        if arr[x] <= pvt:
            i = i + 1
            arr[i], arr[x] = arr[x], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

# Function to do Quick sort 
def quickSort(arr,low,high):
    if len(arr) == 1:
        return arr
    if low < high:
        index = partition(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)




# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n): 
    print(arr[i])
