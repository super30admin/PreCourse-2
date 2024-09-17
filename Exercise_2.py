# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr, low, high):
    i = (low - 1)  # intiate to index that can be considered from the beginning of array
    pivot = arr[high] # pick any pivot. Here we pick from the end

    for j in range(low, high):
        # check if current element is less than the pivot.
        if arr[j] <= pivot:
            i += 1
            # keep swapping these places till we reach arr[low] < arr[high] for every recursive array search
            arr[i], arr[j] = arr[j], arr[i]
    # swap the element with index at high as that is the actual secured place of element in array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # helper function for partition
        part = partition(arr, low, high)

        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

    # Driver code to test above
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
