# Python program for implementation of Quicksort

# Time complexity: worst: O(n^2) best: O(n long n)
# Space complexity : O(n)
# This function is same in both iterative and recursive
def partition(arr,low,high):  
    #write your code here
    i = low-1
    j = low
    pivot = arr[high]
    while i < j and j <= high - 1:
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i
    
    

# Function to do Quick sort 
def quickSortIterative(arr,low,high): 
    #write your code here
    arr_stack = []
    arr_stack.append(low)
    arr_stack.append(high)
    while len(arr_stack) != 0:
      high = arr_stack.pop()
      low = arr_stack.pop()
      if low < high:
        pivot_pos = partition(arr, low, high)
        arr_stack.append(low)
        arr_stack.append(pivot_pos - 1)
        arr_stack.append(pivot_pos + 1)
        arr_stack.append(high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 