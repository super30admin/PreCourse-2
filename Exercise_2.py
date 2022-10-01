# Python program for implementation of Quicksort Sort 
"""
Time Complexity : O(nlogn)
Space Complexity : O(n) recursive call
Any problem you faced while coding this :no
Your code here along with comments explaining your approach
"""

def partition(arr,low,high):


    #write your code here
    """
    This function takes the last item in the list as the pivot and
    returns the right position of the pivot in the list.
    All the items less than the pivot will be at the left and the 
    items greater than the pivot will be at the right of the list
    """
    i = low -1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            #swap the elemets at j and i

            (arr[i],arr[j]) = (arr[j], arr[i])
    #swap the pivot item with the greater item specified by i
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i+1
                        
def quickSort(arr,low,high):
    if arr == []:
        return 

    if low < high :
        # the right partitioned index
        x  = partition(arr, low, high)
        # left side of the pivot recursive call
        quickSort(arr, low, x-1)
        # Right side of the pivot recursive call
        quickSort(arr,x+1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
