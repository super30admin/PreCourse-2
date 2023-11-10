'''
Time Complexity is O(nlogn) average case and O(n^2) in worst case
Space Complexity is O(1) since this is inplace sorting technique so no extra memory space  needed

Explaination 
choose a pivot element
all the elements smaller than pivot elemnts are pushed towards left of pivot
all the elements greater than pivot are moved towards right of pivot
do this approach recursively
'''

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach


def partition(arr,low,high):
    pivot = arr[high]
    pindex = low
    # make all smaller elements to pivot towards left and greater elements towards right
    for i in range(low, high):
        if arr[i]<=pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex+=1
    arr[pindex], arr[high] = arr[high], arr[pindex]
    return pindex



    
  
    #write your code here
    
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        pivot = partition(arr, low, high)  #Get pivot everytime after partition
        quickSort(arr, low, pivot-1)  #Perform operation on left side 
        quickSort(arr, pivot+1, high) #Perform operation on right side
    
    #write your code here
  
# Driver code to test above 
arr = [1,2,3,4] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 