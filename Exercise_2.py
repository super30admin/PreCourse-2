# Python program for implementation of Quicksort Sort

# TODO:
#     Give you explanation for the approach
#     A) Quick sort working:
#     1. generate a partition function which returns the index where array left elements are smaller and array right elements are greater
#     2. after finding partition index, recurse quick sort algorithm, from (low to index-1) and (index + 1 to high), return when high >= low (completed full quicksort)
#     B) Partition function working:
#     Initialize pivot to end element and pivot index to the the beggining
#     if array element is less than pivot, move the element to position before the index element, increment index
#     swap array end element to pivot index. Now we have the final array where all elements to the right of index are greater and left are smaller
#     return the index

# TODO:
#     Time Complexity = Big O(Nˆ2) worst case, Big O(NlogN) best case
#     Space Complexity = Big O(1)

def partition(arr,low,high):
    # arr = [1, 3, 5, 7, 10, 9]
    pivot = arr[high]
    index = low
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[i], arr[index]= arr[index], arr[i]
            index += 1
    arr[index], arr[high] = arr[high], arr[index]
    return index
    #write your code here




# Function to do Quick sort
def quickSort(arr,low,high):
    if high <= low: return
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot + 1, high)

    #write your code here
if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr,0,n-1)
    print ("Sorted array is:")
    for i in range(n):
        print ("%d" %arr[i]),

 
