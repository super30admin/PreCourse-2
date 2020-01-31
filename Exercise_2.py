# Python program for implementation of Quicksort Sort 

def swap (arr, i, j):
    # swap function to swap elements at given indices
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return

# give you explanation for the approach
def partition(arr,low,high):
  
    # O(n) time complexity | O(1) space complexity
    #write your code here
    count = 0                           # count all elements lower than element at low index
    for i in range(low + 1, high + 1):
        if arr[i] < arr[low]:
            count += 1
    swap(arr, low, low + count)

    pivot = low + count

    while (low < pivot and high > pivot):   # push all lower elements to left and all higher elements to right
        if (arr[low] >= arr[pivot]):
            if (arr[high] < arr[pivot]):
                swap(arr, low, high)
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1

    return pivot                        # return the pivot index

# Function to do Quick sort 
def quickSort(arr,low,high): 

    # O(n.logn) Time Complexity | O(1) Space Complexity
    #write your code here
    if (low >= high):       # base case for recursion in quick sort
        return
    pivot = partition(arr, low, high)   # extract the pivot index
    quickSort(arr, low, pivot)          # recursively run from low till before pivot index
    quickSort(arr, pivot+1, high)       # recursively run from after pivot index till high
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

 
