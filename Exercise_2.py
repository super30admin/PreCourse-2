# // Time Complexity : O(n log n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this :No



# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # Considering 1st elem as pivot
    pivot = arr[low]
    # Two pointers 
    pointer_1 = low + 1
    pointer_2 = high

    while True:
        # Stop pointer_1 at the first number greater than or equal pivot
        while pointer_1 <= high and arr[pointer_1] <= pivot:
            pointer_1 += 1
        # Stop pointer_2 at the number smaller than pivot
        while pointer_2 > low and arr[pointer_2] > pivot:
            pointer_2 -= 1
        # Stop the loop when pointer_2 crosses pointer_1
        if pointer_1 >= pointer_2:
            break
        # Swapping the elements at i,j
        arr[pointer_1], arr[pointer_2] = arr[pointer_2], arr[pointer_1]
    # Swapping such that pivot is placed correctly
    arr[low], arr[pointer_2] = arr[pointer_2], arr[low]
    return pointer_2
  


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        # To find the partition index - index of pivot element when placed at right position
        partition_index = partition(arr,low,high)
        # To sort the left unsorted portion
        quickSort(arr, partition_index+1, high)
        # To sort the right unsorted portion
        quickSort(arr, low, partition_index-1)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
