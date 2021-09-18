# Python program for implementation of Quicksort Sort
#Time Complexity = O(n^2) - worst case, O(nlogn) - best case
#Space Complexity = O(logn)


def partition(arr, low, high):

    pivot = arr[high] #assigning pivot as last element

    i = low - 1 # pointer i to index -1

    for j in range(low,high): # run j pointer from start to end of arr
        if arr[j] < pivot: # each time checking if current element is less than pivot
            i = i + 1 #if yes keep incrementing i pointer
            arr[i],arr[j] = arr[j],arr[i] # and swap elements - To make 2 groups (1st grp = elements less then pivot, 2nd grp = elements less then pivot)

    arr[i+1],arr[high] = arr[high],arr[i+1] #At last swap element i+1 index with pivot element - Now pivot element comes in middle

    return i+1 # returning index of pivot

# Function to do Quick sort
def quickSort(arr, low, high):
    if low >= high: # sort is complete or nothing to sort
        return

    p = partition(arr,low,high)

    quickSort(arr,low,p-1) # recursively call QS to left portion of pivot
    quickSort(arr,p+1,high) # recursively call QS to right portion of pivot

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]), 
  
 
