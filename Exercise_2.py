# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# First, I took pivot as the first element
# Then I compared other elements to that pivot and arranged them accordingly
#If lower,then push them to the left of pivot. If higher, then the number is pushed to the right of pivot
# return the end index value of the pivot after each 'partition' function run
# use this pivot index to further recursively perform partitioning on both halfs of the list
def partition(arr,low,high):
    pivot = arr[low]
    left = low+1
    right = high
    while True:
        while left<=right and arr[left] <= pivot:
            left = left+1
        while left<=right and arr[right] >= pivot:
            right = right-1
        if right<left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

    
    #write your code here
  
# Driver code to test above 
arr = [10,7,8,9,1,5]
n = len(arr) 
quickSort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

