# Python program for implementation of Quicksort Sort 
  
"""
Intuition:  Select a pivot element. All the elements on the left of this pivot should be less than the pivot element.
All the elements on the right of this pivot element should be greater than the pivot element

Time Complexity : O(nlog n), Worst case: O(n^2) This depends on the pivot
Space Complexity : O(1)
"""

def partition(arr,low,high):
    
    flag = 0
    pivot = low

    while flag != 1:

        while arr[pivot] <= arr[high] and (pivot != high):
            high -= 1
        
        if pivot == high:
            flag = 1
        
        elif arr[pivot] > arr[high]:
            arr[pivot], arr[high] = arr[high],arr[pivot]
            pivot = high
        
        if flag != 1:

            while arr[low] <= arr[pivot] and(low != pivot):
                low += 1
            
            if pivot == low:
                flag = 1
            elif arr[low] > arr[pivot]:
                arr[low], arr[pivot] = arr[pivot], arr[low]
                pivot = low
    
    return pivot

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot -1)
        quickSort(arr, pivot +1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
