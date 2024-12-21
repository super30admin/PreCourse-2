# Python program for implementation of Quicksort Sort 

# T: O(n^2), S: O(n)
# give you explanation for the approach
def partition(arr,low,high):
    pass
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr): 
    # Base case
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here we choose the last element)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursive call
    # Pivot will always be in the correct spot
    return quickSort(left) + [pivot] + quickSort(right)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
sorted = quickSort(arr) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %sorted[i]), 