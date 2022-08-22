# Python program for implementation of Quicksort Sort 
# TIME COMPLEXITY: # Unfortunately I don't remember
# SPACE COMPLEXITY: O(1) # this is an in-place algorithm
# Did it run in leetcode successfully: Yep
# Any problems faced: Quite a few until I figured out the

# give you explanation for the approach
def partition(arr,low,high):
    # selecting a random index between low and high as a pivot point
    m = random.randint(low, high)
    arr[low], arr[m] = arr[m], arr[low]

    pe = arr[low] # pivot element is first element
    i = low + 1
    j = high
    while i <= j:
        if arr[j] > pe: # this handles repeated elements
            j -= 1
        elif arr[i] <= pe:
            i += 1
        else:
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Function to do Quick sort
def quickSort(arr,low,high):
    p = partition(arr, low, high) # p = partitioning position
    if low < p-1:
        arr = quickSort(arr, low, p-1)
    if p+1 < high:
        arr = quickSort(arr, p+1, high)
    return arr

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
arr = [5, 2, 3, 1]
arr = [2, 2, 1,2, 2, 3, 4, 4, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:", arr)

# for i in range(n):
#     print ("%d" %arr[i]),
  
 
