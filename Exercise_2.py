# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''Idea: find an element(pivot) in the list where the element less that the pivot are placed to the left of the pivot element and
the elements greater than pivot are to the right of the pivot element. This means the picot element is at the correct position in its 
sorted list. Now the subarrys can be sorted by selecting a pivot element and doing the same operations to the subarrays'''

def partition(arr,low,high):
    
    pivot = arr[high] 
    # i function like a wall seperating the elements lesser and greater than the pivot element and j would iterate the subarray until it reaches the pivot element
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Once the smaller elements have been moved to the left, we swap the position of the pivot just after these elements such that elements lesser than and greater than pivot are seperated
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    print(low,' ', high)
    if low < high:
        p = partition(arr, low, high)
        # Sorting left and right subarrays recursively
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
 
