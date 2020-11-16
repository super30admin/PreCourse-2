# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#write your code here
def partition(arr,low,high): 
    i = ( low-1 )    
    pivot_element = arr[high]     #Taking Last element as pivot element
                                #Elements smaller than pivot on comparison with current will be stored left of pivot
                                # and greater than on the right of pivot 
    for j in range(low , high): 
        if  arr[j] < pivot_element: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
     if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
if n<=1:                        #If length of array is 1 print array else sort
        print (arr)
else:
    quickSort(arr,0,n-1)  #low=0 (Starting index); high=n-1 (leength of array-1-end index)
    print ("Sorted array is:") 
    for i in range(n):
        print ("%d" %arr[i]), 

# The other way of coding is choosing pivot as the 
# last element and than elements smaller than pivot will be stored in left side in items_smaller array
# elemnts greater than pivot will be stored in items_greater array

"""
  def quickSort(arr):
    items_greater=[]
    items_smaller=[]
    length=len(arr)
    if length<=1:
          return arr
    else:
          pivot=arr.pop()
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)
    return quickSort(items_smaller)+[pivot]+quickSort(items_greater)
    """
 
