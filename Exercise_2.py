# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #we always pick the last element as pivot
    i = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[high] = arr[high],arr[i]
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pindex = partition(arr,low,high)

        quickSort(arr,low,pindex-1)
        quickSort(arr,pindex+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])