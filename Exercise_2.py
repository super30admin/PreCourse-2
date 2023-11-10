# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# Here, i'm choosing the first element to be the pivot.
# Initially, we set i to the 2nd element and j to last element. 
# Then, we move i towards the right and j towards the left of the array in such a manner that elements larger than the pivot are on it's right and lower are on it's left. - This is done in the partition().
# Now, we swap our pivot and j to get the correct position of the pivot. Now, things to the right of pivot are higher than it and left are lower, however, these elements might not be ordered. So, we recursively call till all elements are sorted.
def partition(arr,low,high):

    pivot=arr[low]
    i=low+1
    j=high

    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>=pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
        
    arr[low],arr[j]=arr[j],arr[low]

    return j


# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low<high:
        pivot=partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)
    
    return

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
