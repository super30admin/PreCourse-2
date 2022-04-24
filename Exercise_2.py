# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#partition function takes in the sub-array and selects the rightmost element as the pivot 
#partition the array such that all elements less than pivot are to the left of it 
#and elements greater than pivot are to the right of it.
#this function returns the partition index (index at which the array must be divided into two sub-arrays)

#Time complexity - O(n^2)
#Space complexity - O(logn)

def partition(arr,low,high):
    i=low-1          #index (pointer) to larger element
    pivot=arr[high]  #pivot
    
    #traverse through the array, comparing each element with the pivot

    for j in range(low,high):
        #if element less than pivot is found,swap it with larger element pointed by i
        if arr[j]<=pivot:
            i=i+1
            #swapping
            arr[j],arr[i]=arr[i],arr[j]
    #position the pivot at the right place after sorting.
    arr[i+1],arr[high]=arr[high],arr[i+1]
    #return partition index 
    return i+1

    
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #checking base case 
    if low<high:
        #get the partition index
        partition_index=partition(arr,low,high)
        #sort the left subarray
        quickSort(arr,low,partition_index-1)
        #sort the right subarray
        quickSort(arr,partition_index+1,high)
    
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

 
