# Python program for implementation of Quicksort Sort 
#Time Complexity: O(nlogn)
#Space Complexity: O(1)
# give your explanation for the approach:
'''
Initially, I considered the first element as my 'pivot' element with which I compared all the other
elements in the list.
By swapping elements accordingly, I found the real position of the 'pivot' element. This meant that all the elements
to the left of the 'pivot' element are less than it and the right of the 'pivot' element are greater than it.
This process is repeated until all the elements are sorted.
'''

def partition(arr,start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

# Function to do Quick sort 
def quickSort(arr,start, end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)
    #write your code here
if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr,0,n-1)
    print ("Sorted array is:")
    for i in range(n):
        print ("%d" %arr[i]),
  
 
