# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low] #Assign pivot
    low1 = low + 1 # Assign lowest elements
    high1 = high  # Assign highest elements

    while True:

        """If the current element is larger than the pivot
        it's in the right side of pivot and we can move to the next element"""

        while low1 <= high1 and arr[high1] >= pivot:
            high1 = high1 - 1

        while low1 <= high1 and arr[low1] <= pivot:
            low1 = low1 + 1

        """Now we find a value for both high and low that is invalid
        or
        low is greater than high so, we exit the loop"""

        if low1 <= high1:
            arr[low1], arr[high1] = arr[high1], arr[low1]
        else:
            break

    arr[low], arr[high1] = arr[high1], arr[low]

    return high1

# Function to do Quick sort
def quickSort(arr,low,high):
    if low >= high:
        return

    divide = partition(arr, low, high)
    quickSort(arr, low, divide - 1)
    quickSort(arr, divide + 1, high)
  
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i])
