#TimeComplexity: O(nlogn)
#SpaceComplexity: O(1)
def partition(arr,low,high):

    pivot = arr[high] # set last item to pivot
    ptr = low         # first to pointer
    for i in range(low, high):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
   
    arr[ptr], arr[high] = arr[high], arr[ptr] # swappping the last element with the pointer indexed number
    return ptr
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:  
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)  # Recursively sorting the left values
        quickSort(arr, pi+1, high)  # Recursively sorting the right values
    return arr
    #write your code here
  
# Driver code to test above 
arr = [3, 7, 8, 9, 11, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
