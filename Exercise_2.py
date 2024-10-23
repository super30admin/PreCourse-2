# Python program for implementation of Quicksort Sort


# give you explanation for the approach
# iN this approach last element is selected as pivot element
# all the leemnts less than pivot are partitioned to left and all elements to teh right are partitioned to right side of the array
#Partition takes O(n time) and this is done log n times so it is O(nlogn)
def partition(arr, low, high):
        # write your code here
    pivot = arr[high]
    left = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    arr[high], arr[left] = arr[left], pivot
    return left




# Function to do Quick sort
def quickSort(arr, low, high):

    # write your code here
    if high - low +1 <= 1:
        return
    left = partition(arr, low, high)
    quickSort(arr, low, left-1)
    quickSort(arr, left+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5, 6, 13]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
