# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]

    for j in range (low, high):
        if arr[j] <= pivot:
            i = i + 1

            #SWAP i, j
            arr[i], arr[j] = arr[j], arr[i]

    # SWAP i +1 and Pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i+1)


        # write your code here


# Function to do Quick sort
def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr
    elif low < high:
        pivot = partition(arr,low,high)
        quickSort(arr,low, pivot-1)
        quickSort(arr,pivot+1,high)



# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5,2,3,5,213,2,32,3,23,7,56,7,3,31,34,3]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])