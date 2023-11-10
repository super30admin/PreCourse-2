# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#Partition function is used to select the pivot element position
#quicksort is applied on the elements to the left of pivot position and then to the right

# To partition:( return pivot index with elements to the
# left are less than pivot value and to the right are greater than pivot value)
#Last element is chosen as pivot
# i (goes left to right) tracks for the element greater than pivot and j(right-1 to left) tracks for element less than pivot
# when i and j doesnt cross over each other swap values at i and j
# else swap i and pivot values and return pivot value


def partition(arr,low,high):
    i = low
    j = high - 1
    pivot = arr[high]
    while i < j:
        while i<high and arr[i]<pivot:
            i += 1
        while j>low and arr[j]>=pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        partPos = partition(arr, low, high)
        quickSort(arr, low, partPos-1)
        quickSort(arr, partPos+1, high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 #Time Complexity: O(n^2)
 #Space Complexity: O(1) as no extra space is needed

