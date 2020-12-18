# Python program for implementation of Quicksort using Recursive method
# Time Complexity - Best & Average -- O(Nlog(N)) -- when pivot subdivdes arr into almost 2 equal sub sections
#                 - Worst --- O(N^2) -- when pivot subdivides arr into one large arr of ~(n-1) and one small arr
# Space Complexity - O(log(N))
# Successively ran 

# Approach: 
#   1. Pick pivot (as first element) in array and set left and right pointers denoting start and end of arr
#   2. When the element at left idx and right to pivot is greater than AND less than respectively, swap those numbers
#   3. Continue checking if left of pivot is less than or equal to pivot and right if greater or equal to pivot
#   4. Based on (3) increment left or decrement right accordingly and at one stage the pointers pass each other
#   5. At this stage swap right and pivot. Now pivot is at its sorted positon in the array
#   6. Once pivot is in its sorted position, perform quick sort recursively on both left and right sub arrays.
#   7. Perform recursion on smaller array first to save frames used on call stack, then recur on bigger arrray
# Repeat

def partition(arr, low, high):

    pivotIdx = low
    leftIdx = low + 1
    rightIdx = high

    while rightIdx >= leftIdx:
        
        if arr[leftIdx] > arr[pivotIdx] and arr[rightIdx] < arr[pivotIdx]:
            swap(leftIdx, rightIdx, arr)
            
        if arr[leftIdx] <= arr[pivotIdx]:
            leftIdx += 1
            
        if arr[rightIdx] >= arr[pivotIdx]:
            rightIdx -= 1
            
    swap(pivotIdx, rightIdx, arr)
    return rightIdx #This is the index where pivot element is moved to

def quickSort(arr, low, high):

    # check for 2 base cases if arr has 1 element only, return it
    if len(arr) == 1:
        return array
    
    if low >= high:
        return
    
    # obtain pivot idx by partition
    pivotIdx = partition(arr, low, high)

    # divide left and right subarrays based on pivot
    leftSubArray = pivotIdx - 1 - (low) 
    rightSubArray = high - (pivotIdx + 1)
    
    # To optimize tail recursion perform the recursive call on smaller sub array to save frames used on call stack then proceed to larger subarray
    
    if leftSubArray < rightSubArray :
        quickSort(arr, low, pivotIdx -1) # recur smaller array first
        quickSort(arr, pivotIdx + 1, high)
    
    else:
        quickSort(arr, pivotIdx + 1, high)
        quickSort(arr, low, pivotIdx -1)

# helper function to swap elements at indices
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# driver code
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),
        
      

 
