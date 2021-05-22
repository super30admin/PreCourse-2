# Python program for implementation of Quicksort Sort 
'''
Time complexity: O(n)
Space complexity O(n)
'''
# give you explanation for the approach
def partition(arr,low,high):
    
    # we need to make sure to return the point of partition
    pivot_point = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot_point:
            # you need to swap out i first before assigning
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # one last pass
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1: return arr

    #write your code here
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" % arr[i])
  
 
