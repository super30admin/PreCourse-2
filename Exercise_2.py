# Python program for implementation of Quicksort Sort 
  
"""  
Time complexity : O(n*log(n))
Space complexity : O(n) 

explanation: 

in this approach, with the given array, If low value is greater than or equal to high, that means the array length 
is zero and I have to return nothing. 
or else I'll call a function named 'partition' which returns the correct index of an element which will be in the sorted array 
let's assign the value of p as the value returned from partition function. 

in partition function, this is what we do: 
we'll assign the right most element (high) as our pivot and a pointer named 'i' will be the element before the left most.
now we'll open a iterator loop from low to high and we'll check if the element is greater than pivot or not. 
if the element is greater than pivot or equal than pivot, we don't disturb it.
if the element is lesser than pivot, we'll swap it with current greater element (currently where the iterator is) 
we will repeat it until we have the elements smaller than pivot in the left and elements greater than or equal to pivot on the right hand side 
once this is done, the iterator loop ends 
now we'll swap the pivot in between those two groups (group which is smaller than pivot and group which is larger than pivot) 
once swapped, the index of the pivot must be returned as it will be the permanent correct index of the pivot. 
this is repeated until the array is completely sorted 

once we have the value of p, we'll now sort the left elements of p and sort right elements of p by recursively calling 
quicksort function which recursively calls the partition function again and again 

""" 

def partition(arr,low,high):
    
    pivot = arr[high]
    i = low - 1 
    for j in range(low, high): 
        if arr[j]<pivot: 
            i+=1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[high], arr[i+1] = arr[i+1], arr[high] 
    return i+1


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low>=high: 
        return   

    p = partition(arr,low,high) 

    quickSort(arr,low,p-1) 
    quickSort(arr,p+1,high)

  
# Driver code to test above 
arr = [2,4,43,2,2,2,2,33,4,2,1,1,1,2,3,3,3,4,5,7,6,4,3,5,7,5,4,3] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
