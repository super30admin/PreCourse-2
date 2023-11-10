# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
## Firstly, we define as pivot as the last element. Then, we define one counter as i =-1 and loop through elements till
## pivot -1 . if the elements is greater than pivot, we do nothing otherwise we increment i and swap elements at i and j.
## Finally we swap element at i+1 and pivot so that we partition the arr according to pivot. We countinue for 2 sub arrays
## till we achieve the final sorted array.

## Space Complexity = O(1)
## Time Complexity = O(n)

def partition(arr, low, high):
    # write your code here
    pivot = high
    i = -1

    for j in range(0, pivot):
        if arr[j] > arr[pivot]:
            continue
        else:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

    return i + 1


# Function to do Quick sort
def quickSort(arr, low, high):
    # write your code here

    if low < high:
        p = partition(arr, low, high)
        print(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


# Driver code to test above
arr = [10, 2, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i]),


