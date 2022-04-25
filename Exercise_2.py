# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    i = low-1
    #Taking pivot as last element
    pivot = arr[high]
    #Iterating from low to high
    for j in range(low,high):
        #If the element is less than pivot, increase the i index and swap with jth element.
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    #Swap the i+1th index element with high index element and return the i+1 index.
    # The elements before the i+1th index are less than the pivot and elements after i+1th index are greater than pivot. 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        #Calls the partition function to get the index of pivot.
        q = partition(arr,low,high)
        #Recursive call of array left to the pivot.
        quickSort(arr,low,q-1)
        #Recursive call of array right to the pivot.
        quickSort(arr,q+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
