# Python program for implementation of Quicksort Sort 
  
# Time complexity for quick sort is O(n log n) and space complexity is O(n)

# In partition function, we set pivot to right most value in array i.e. 5 in this case from [10, 7, 8, 9, 1, 5]. 
# Initially, low is 0 and high is 5. Then we loop over the array to see if jth value is less than pivot value, if yes,
# we swap the jth value with the ith value in case of 1 < 5, arr[4] and arr[0] got swapped to get [1, 7, 8, 9, 10, 5] and i gets incremented to 1. 
# If nothing else is within range as in this case, then we swap the pivot with i[1] in this to get [1, 5, 8, 9, 10, 7]. 
# Then, we recursively sort left side array first to make it [1, 5, 7, 9, 10, 8] i.e. pivot gets moved here since.
# Then similarly, pivot 8 moves to make it [1, 5, 7, 8, 10, 9] and then finally after swapping last positions we get the output.

def partition(arr,low,high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    temp = arr[i]
    arr[i] = arr[high]
    arr[high] = temp
    return i
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if not arr:
        return

    while low < high:
        pivot = partition(arr, low, high)
        if pivot - low < high - pivot:
            quickSort(arr, low, pivot - 1)
            low = pivot + 1
        else:
            quickSort(arr, pivot + 1, high)
            high = pivot - 1
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 