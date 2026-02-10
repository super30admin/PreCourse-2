# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Quick sort is a devide and conqure approach. basically we choose a starting point and then try to place it in 
# it's correct position, i.e all the numbers on left are small and right are big.
# Once we that number is in correct place, we devide the array into 2 half from the point (not including that poin)
# and recursively start finding the correct position of 1 elment in the sub array and so on untill all elments are 
# in it's correct position
def partition(arr,low,high):

    # This helper is used to arrange 1 number in it's corrrect positino and return the new index of that point
    # the new index will become point for breaking the array into sub arrays
  
    j = low
    i = low -1
    pivot = arr[high] #the number we are trying to correct place, let's pick last element

    while j<=high:
        if arr[j]<=pivot:
            i+=1
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
        j+=1
    return i

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low>=high:
        return

    pivot = partition(arr,0,high)

    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot+1, high)

    #write your code here
  
# Driver code to test above 
arr = [6,5,4,3,2,1] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
