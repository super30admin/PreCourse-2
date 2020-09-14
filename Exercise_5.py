# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
    pivot = arr[high]
    i = low

    for m in range(low, high):
        if arr[m] <= pivot:
            arr[i], arr[m] = arr[m], arr[i]
            i += 1
            

    arr[i] , arr[high] = arr[high], arr[i]
    return arr, i

def quickSortIterative(arr, l, h):
  #write your code here
    pass


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
