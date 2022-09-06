# Python program for implementation of Quicksort Sort 

# I watched youtube to learn about the algorithm
# I do not know how to code in the first place
# this is the first time I am coding
# I tried to understand what it meant but its not easy

def partition(arr, low, high):
    pt, p = low, arr[high]
    for i in range(low, high):
        if arr[i] <= p:
            arr[i], arr[pt] = arr[pt], arr[i]
            pt = pt + 1
    arr[pt], arr[high] = arr[high], arr[pt]
    return pt


# Function to do Quick sort 
def quickSort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
